import math
from copy import deepcopy

left_late = 0
top_late = 0.4
right_late = 1
bottom_late = 1
border_rect = []

class TraceFrame:
    def __init__(self, frame):
        self.height, self.width = frame[:2]
        self.objects = []
        border_rect.extend([self.width*left_late, self.height*top_late, self.width*right_late, self.height*bottom_late])

    def append_object(self, detects) -> None:
        for detect in detects:
            _object = Trajectory(detect.to("cpu").detach().numpy().copy())
            _object.update_status()
            self.objects.append(deepcopy(_object))

    def __del__(self):
        border_rect = []


class Trajectory:
    def __init__(self, detect):
        self.next = None
        self.prev = None
        self.status = None
        self.left_upper = (detect[:2])
        self.right_lower = (detect[2:4])
        self.confidence = detect[4]
        self.class_id = int(detect[5])

    def update_status(self):
        target_x = self.get_center_x()
        target_y = self.get_center_y()
        x_flag = border_rect[0] <= target_x <= border_rect[2]
        y_flag = border_rect[1] <= target_y <= border_rect[3]
        self.status = bool(x_flag and y_flag)

    def get_center_x(self) -> float:
        return (self.left_upper[0] + self.right_lower[0]) / 2

    def get_center_y(self) -> float:
        return (self.left_upper[1] + self.right_lower[1]) / 2

    def get_center_point(self) -> tuple:
        return (self.get_center_x(), self.get_center_y())

    def calc_distance(self, target) -> float:
        x_1 = self.get_center_x()
        y_1 = self.get_center_y()
        x_2 = target.get_center_x()
        y_2 = target.get_center_y()
        return math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)

    def contains(self, target) -> bool:
        target_x = target.get_center_x()
        target_y = target.get_center_y()
        x_flag = self.left_upper[0] <= target_x and target_x <= self.right_lower[0]
        y_flag = self.left_upper[1] <= target_y and target_y <= self.right_lower[1]
        return x_flag and y_flag

    def find_connect_point(self, prev_objects):
        distance = 10**100
        point = None
        for object in prev_objects:
            if self.contains(object) and object.next == None and self.class_id == object.class_id:
                pre_distance = self.calc_distance(object)
                if distance > pre_distance:
                    distance = pre_distance
                    point = object
        return point
