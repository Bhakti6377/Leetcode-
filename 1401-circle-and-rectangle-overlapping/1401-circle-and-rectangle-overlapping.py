class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        # Find the closest point on the rectangle
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = closestX - xCenter
        dy = closestY - yCenter

        # Check if the point lies inside the circle
        return dx * dx + dy * dy <= radius * radius       