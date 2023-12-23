```python
import numpy as np

class PathPlanning:
    def __init__(self):
        pass

    def calculate_path(self, start_coordinates, destination_coordinates):
        # For the purpose of this simulation, we'll just move the object in a straight line
        current_coordinates = np.array(start_coordinates)
        path = [current_coordinates]

        while not np.array_equal(current_coordinates, destination_coordinates):
            # Calculate the direction vector
            direction_vector = destination_coordinates - current_coordinates
            direction_vector = direction_vector / np.linalg.norm(direction_vector)

            # Move the object along the direction vector
            current_coordinates += direction_vector
            path.append(current_coordinates)

        return path

    def check_for_obstacles(self, path):
        # In this simulation, we'll assume there are no obstacles
        return False

    def plan_path(self, start_coordinates, destination_coordinates):
        # Calculate the path
        path = self.calculate_path(start_coordinates, destination_coordinates)

        # Check for obstacles
        if self.check_for_obstacles(path):
            raise Exception('Obstacle detected in the path!')

        return path

if __name__ == "__main__":
    path_planning = PathPlanning()
    path = path_planning.plan_path(np.array([0, 0, 0]), np.array([10, 10, 10]))
    print('Path:', path)
```
