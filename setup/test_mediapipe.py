import cv2
import numpy as np
import mediapipe as mp
import time

dev = 0

def main():
    mymp = myMediapipe()

    cap = cv2.VideoCapture(dev)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    sr = int(1000/fps)

    flags = {'mesh': False, 'pose': False, 'hands': False, 'face': False, 'iris': False, 'segment': False}

    fno = 0
    prv = time.perf_counter()
    while cap.isOpened():
        ret, frame = cap.read()
        image = mymp.getMPImage(frame)

        now = time.perf_counter()
        pst = int((now-prv)*1000)
        fno = fno + 1 + (pst//sr)
        sfps = min(int(fps), 1000//pst)

        key = cv2.waitKey(max(1, sr-pst))
        if ret == False or key == ord('q'):
            break

        if key == ord('m') or key == ord('a'):
            flags['mesh'] = ~flags['mesh']
        if key == ord('p') or key == ord('a'):
            flags['pose'] = ~flags['pose']
        if key == ord('h') or key == ord('a'):
            flags['hands'] = ~flags['hands']
        if key == ord('f') or key == ord('a'):
            flags['face'] = ~flags['face']
        if key == ord('i') or key == ord('a'):
            flags['iris'] = ~flags['iris']
        if key == ord('s') or key == ord('a'):
            flags['segment'] = ~flags['segment']        

        if flags['mesh']:
            plist = mymp.getFaceMesh(image, wt, ht)
            if plist is not None:
                if len(plist)==478:
                    for id1, id2 in mymp.getConnections('mesh'):
                        cv2.line(frame, (int(plist[id1][0]), int(plist[id1][1])), (int(plist[id2][0]), int(plist[id2][1])), [255,255,255], 2)
                for p in plist[:468]:
                    cv2.circle(frame, (int(p[0]), int(p[1])), 3, [0, 255, 0], -1)

        if flags['pose']:
            plist = mymp.getPose(image)
            if plist is not None:
                if len(plist)==33:
                    for id1, id2 in mymp.getConnections('pose'):
                        cv2.line(frame, (int(plist[id1][0]), int(plist[id1][1])), (int(plist[id2][0]), int(plist[id2][1])), [255,255,255], 2)
                for p in plist:
                    cv2.circle(frame, (int(p[0]), int(p[1])), 3, [255, 0, 255], -1)

        if flags['face']:
            frect, plist = mymp.getFace(image, wt, ht)
            if plist is not None:
                cv2.rectangle(frame, (frect[0], frect[1]), (frect[0]+frect[2], frect[1]+frect[3]), [255,255,255], 2)
                for p in plist:
                    cv2.circle(frame, (int(p[0]), int(p[1])), 3, [0, 0, 255], -1)

        if flags['hands']:
            plist = mymp.getHand(image, wt, ht)
            if plist is not None:
                landmarks_r = plist['right']
                landmarks_l = plist['left']

                if len(landmarks_r)==21:
                    for id1, id2 in mymp.getConnections('hands'):
                        cv2.line(frame, (int(landmarks_r[id1][0]), int(landmarks_r[id1][1])), (int(landmarks_r[id2][0]), int(landmarks_r[id2][1])), [255,255,255], 2)
                for p in landmarks_r:
                    cv2.circle(frame, (int(p[0]), int(p[1])), 3, [0, 255, 0], -1)

                if len(landmarks_l)==21:
                    for id1, id2 in mymp.getConnections('hands'):
                        cv2.line(frame, (int(landmarks_l[id1][0]), int(landmarks_l[id1][1])), (int(landmarks_l[id2][0]), int(landmarks_l[id2][1])), [255,255,255], 2)
                for p in landmarks_l:
                    cv2.circle(frame, (int(p[0]), int(p[1])), 3, [255, 0, 0], -1)

        if flags['iris']:
            plist = mymp.getIris(image, wt, ht)
            if plist is not None:
                lp2d = np.array([(p[0], p[1]) for p in plist['leye']])
                rp2d = np.array([(p[0], p[1]) for p in plist['reye']])
                (x,y),radius = cv2.minEnclosingCircle(lp2d)
                cv2.circle(frame, (int(x), int(y)), int(radius), [0, 255, 255], 2)
                (x,y),radius = cv2.minEnclosingCircle(rp2d)
                cv2.circle(frame, (int(x), int(y)), int(radius), [0, 255, 255], 2)

        if flags['segment']:
            sg = mymp.getSegmentImage(image)
            frame[sg==False] = 255

        cv2.putText(frame, str(sfps)+"/"+str(fno), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
        cv2.imshow('video', frame)
        prv = now

    cap.release()
    cv2.destroyAllWindows()

class myMediapipe:
   def __init__(self, detection=0.2, tracking=0.2):
       global hands, pose, fmesh, face, segment

       self.hands = mp.solutions.hands.Hands(min_detection_confidence = detection, 
                                             min_tracking_confidence = tracking)
       self.pose = mp.solutions.pose.Pose(static_image_mode = False, 
                                          model_complexity = 1, 
                                          enable_segmentation = False, 
                                          min_detection_confidence = detection, 
                                          min_tracking_confidence = tracking)
       self.fmesh = mp.solutions.face_mesh.FaceMesh(static_image_mode = False, 
                                                    max_num_faces = 1, 
                                                    refine_landmarks = True, 
                                                    min_detection_confidence = detection)
       self.face = mp.solutions.face_detection.FaceDetection(model_selection = 0, 
                                                             min_detection_confidence = detection)
       self.segment = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection = 0)

   def getMPImage(self, frame):
       mp_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

       return mp_image

   def getFace(self, image, wt, ht, getkeys=True):
       results = self.face.process(image)
       point_list = []
       face_box = []
       if results.detections is not None:
           for detection in results.detections:
               bbox = detection.location_data.relative_bounding_box
               face_box = [int(bbox.xmin*wt), int(bbox.ymin*ht), int(bbox.width*wt), int(bbox.height*ht)]
               keys = [[max(1, min(int(landmark.x * wt), wt-1)), max(1, min(int(landmark.y * ht), ht-1))] for landmark in detection.location_data.relative_keypoints]
               point_list = [face_box, keys]

       return point_list

   def getFaceMesh(self, image, wt, ht, getkeys=True):
       results = self.fmesh.process(image)
       point_list = []
       if results.multi_face_landmarks is not None:
           for one_face_landmarks in results.multi_face_landmarks:
               tmp = [[max(1, min(int(landmark.x * wt), wt-1)), max(1, min(int(landmark.y * ht), ht-1)), int(landmark.z * wt)] for landmark in one_face_landmarks.landmark]
               point_list = tmp

       return point_list
   
   def getIris(self, image, wt, ht, getkeys=True):
       results = self.fmesh.process(image)
       lpoint_list = []
       rpoint_list = []
       if results.multi_face_landmarks is not None:
           for one_face_landmarks in results.multi_face_landmarks:
               tmp = [[max(1, min(int(landmark.x * wt), wt-1)), max(1, min(int(landmark.y * ht), ht-1)), int(landmark.z * wt)] for landmark in one_face_landmarks.landmark[-10:-5]]
               lpoint_list = tmp
               tmp = [[max(1, min(int(landmark.x * wt), wt-1)), max(1, min(int(landmark.y * ht), ht-1)), int(landmark.z * wt)] for landmark in one_face_landmarks.landmark[-5:]]
               rpoint_list = tmp

       return {'leye': lpoint_list, 'reye': rpoint_list}

   def getHand(self, image, wt, ht):
       tmp = cv2.flip(image, 1)
       results = self.hands.process(tmp)
       hpoint_list = None
       lhand_points = []
       rhand_points = []

       if results.multi_hand_landmarks is not None:
           for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
               if results.multi_handedness[i].classification[0].label == "Left":
                   for i, landmark in enumerate(hand_landmarks.landmark):
                       x = max(1, min(int(landmark.x * wt), wt-1))
                       y = max(1, min(int(landmark.y * ht), ht-1))
                       lhand_points.append([int(abs(x-wt)), int(y), landmark.z])
               elif results.multi_handedness[i].classification[0].label == "Right":
                   for i, landmark in enumerate(hand_landmarks.landmark):
                       x = max(1, min(int(landmark.x * wt), wt-1))
                       y = max(1, min(int(landmark.y * ht), ht-1))
                       rhand_points.append([int(abs(x-wt)), int(y), landmark.z])
           hpoint_list = {'left': lhand_points, 'right': rhand_points}
       return hpoint_list

   def getPose(self, frame): # Mediapipe can detect only one person.
       ht, wt, _ = frame.shape
       results = self.pose.process(frame)
       pose_points = []
       pose_list = []
       if results.pose_landmarks is not None:
           for i, point in enumerate(results.pose_landmarks.landmark):
               x = max(1, min(int(point.x * wt), wt-1))
               y = max(1, min(int(point.y * ht), ht-1))
               z = int(point.z * wt)
               pose_points.append([x, y, z, point.visibility])
           pose_list = pose_points
       return pose_list

   def getSegmentImage(self, frame, dep=0.1):
       condition = []
       sresults = self.segment.process(frame)

       if sresults.segmentation_mask is not None:
           condition = np.stack((sresults.segmentation_mask,)*3, axis=-1) > dep

       return condition

   def getConnections(self, solution_name):
       if solution_name=='hands':
           return mp.solutions.hands.HAND_CONNECTIONS
       elif solution_name=='pose':
           return mp.solutions.pose.POSE_CONNECTIONS
       elif solution_name=='mesh':
           return mp.solutions.face_mesh.FACEMESH_TESSELATION


if __name__=='__main__':
    main()