from setuptools import setup

package_name = 'merge_arrays'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "merge_arrays_node=merge_arrays.merge_arrays_node:main",
            "test_publish_node=merge_arrays.test_publisher:main",
            "test_listen_node=merge_arrays.test_listener:main"
        ],
    },
)
