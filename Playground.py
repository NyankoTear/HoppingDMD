import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
p.loadURDF("plane.urdf")
p.loadURDF("test.urdf", [0, 0, 0], useFixedBase = True)
pts = p.getContactPoints()
while(True):
  p.setRealTimeSimulation(1)