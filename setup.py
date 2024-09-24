from setuptools import setup

package_name = 'autonomous_vehicle'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='R.U.N.S',
    maintainer_email='eng23ra0065@dsu.edu.in',
    description='An autonomous vehicle project using Raspberry Pi and ROS 2.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_control = autonomous_vehicle.motor_control:main',
            'lidar_node = autonomous_vehicle.lidar_node:main',
            'camera_node = autonomous_vehicle.camera_node:main',
        ],
    },
)
