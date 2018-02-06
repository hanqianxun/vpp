from setuptools import setup

setup(name="vpp_config",
      version="18.01.4",
      author="John DeNisco",
      author_email="jdenisco@cisco.com",
      description="VPP Configuration Utility",
      license = 'Apache-2.0',
      keywords="vppconfig",
      url = 'https://wiki.fd.io/view/VPP',
      py_modules=['vpp_config'],
      install_requires=['pyyaml','netaddr'],
      packages=['vpplib'],
      scripts=['scripts/vpp-config'],
      data_files=[('vpp/vpp-config/scripts', ['scripts/dpdk-devbind.py']),
                  ('vpp/vpp-config/configs', ['data/auto-config.yaml']),
                  ('vpp/vpp-config/configs', ['data/cloud-config.iso']),
                  ('vpp/vpp-config/configs', ['data/iperf-centos.xml.template']),
                  ('vpp/vpp-config/configs', ['data/iperf-ubuntu.xml.template']),
                  ('vpp/vpp-config/dryrun/sysctl.d', ['data/80-vpp.conf.template']),
                  ('vpp/vpp-config/dryrun/default', ['data/grub.template']),
                  ('vpp/vpp-config/dryrun/vpp', ['data/startup.conf.template']),
      ],
      long_description="The VPP configuration utility can be used to easily configure VPP.",
      )
