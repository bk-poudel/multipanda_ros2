import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bibek/Summer_Research/multipanda_ros2/install/franka_simple_publishers'
