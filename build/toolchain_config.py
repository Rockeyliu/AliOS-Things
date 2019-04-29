# Download toolchain automatically
auto_download = "yes"

# Available toolchains
toolchains = {
    'arm-none-eabi':{
        'name': 'gcc-arm-none-eabi',
        'path': 'build/compiler/gcc-arm-none-eabi',
        'command': 'arm-none-eabi-gcc',
        'version': 'all',
        'use_global': True,
        'Win32_url':'https://gitee.com/alios-things/gcc-arm-none-eabi-win32.git',
        'Linux32_url': 'https://gitee.com/alios-things/gcc-arm-none-eabi-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/gcc-arm-none-eabi-linux.git',
        'OSX_url': 'https://gitee.com/alios-things/gcc-arm-none-eabi-osx.git',
        },
    'xtensa-esp32':{
        'name': 'gcc-xtensa-esp32',
        'path': 'build/compiler/gcc-xtensa-esp32',
        'command': 'xtensa-esp32-elf-gcc',
        'version': '5.2.0',
        'use_global': True,
        'Win32_url': 'https://gitee.com/alios-things/gcc-xtensa-esp32-win32.git',
        'Linux32_url': 'https://gitee.com/alios-things/gcc-xtensa-esp32-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/gcc-xtensa-esp32-linux.git',
        'OSX_url': 'https://gitee.com/alios-things/gcc-xtensa-esp32-osx.git',
        },
    'xtensa-lx106':{
        'name': 'gcc-xtensa-lx106',
        'path': 'build/compiler/gcc-xtensa-lx106',
        'command': 'xtensa-lx106-elf-gcc',
        'version': '4.8.2',
        'use_global': True,
        'Win32_url': 'https://gitee.com/alios-things/gcc-xtensa-lx106-win32.git',
        'Linux32_url': 'https://gitee.com/alios-things/gcc-xtensa-lx106-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/gcc-xtensa-lx106-linux.git',
        'OSX_url': 'https://gitee.com/alios-things/gcc-xtensa-lx106-osx.git',
        },
    'csky-abiv2': {
        'name': 'gcc-csky-abiv2',
        'path': 'build/compiler/gcc-csky-abiv2',
        'command': 'csky-abiv2-elf-gcc',
        'version': 'all',
        'use_global': True,
        'Win32_url': 'https://gitee.com/alios-things/gcc-csky-abiv2-win32.git',
        'Linux32_url': 'https://gitee.com/alios-things/gcc-csky-abiv2-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/gcc-csky-abiv2-linux.git',
        'OSX_url': '',
        },

    'arm-rockchip-linux-gnueabihf': {
        'name': 'gcc-arm-rockchip-linux-gnueabihf',
        'path': 'build/compiler/usr',
        'path_specific': True,
        'command': 'arm-rockchip-linux-gnueabihf-gcc',
        'version': 'all',
        'use_global': True,
        'Win32_url': '',
        'Linux32_url': 'https://gitee.com/alios-things/arm-rockchip-linux-gnueabihf-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/arm-rockchip-linux-gnueabihf-linux.git',
        'OSX_url': '',
        },

    'nds32le-elf-newlib-v3': {
        'name': 'nds32le-elf-newlib-v3',
        'path': 'build/compiler/nds32le-elf-newlib-v3',
        'path_specific': True,
        'command': 'nds32le-elf-gcc',
        'version': 'all',
        'use_global': True,
        'Win32_url': '',
        'Linux32_url': 'https://gitee.com/alios-things/gcc-nds32le-linux.git',
        'Linux64_url': 'https://gitee.com/alios-things/gcc-nds32le-linux.git',
        'OSX_url': '',
        },
}

# Board and toolchain mapping
boards = {
    'aaboard_demo':[toolchains['arm-none-eabi']],
    'amebaz_dev':[toolchains['arm-none-eabi']],
    'ap80a0':[toolchains['arm-none-eabi']],
    'atsame54-xpro':[toolchains['arm-none-eabi']],
    'b_l475e':[toolchains['arm-none-eabi']],
    'bk7231devkitc':[toolchains['arm-none-eabi']],
    'bk7231udevkitc':[toolchains['arm-none-eabi']],
    'cy8ckit-062':[toolchains['arm-none-eabi']],
    'developerkit':[toolchains['arm-none-eabi']],
    'eml3047':[toolchains['arm-none-eabi']],
    'es8p5088fllq':[toolchains['arm-none-eabi']],
    'evkbimxrt1050':[toolchains['arm-none-eabi']],
    'evkmimxrt1020':[toolchains['arm-none-eabi']],
    'esp32devkitc':[toolchains['xtensa-esp32']],
    'esp8266':[toolchains['xtensa-lx106']],
    'esp8285':[toolchains['xtensa-lx106']],
    'fm33a0xx-discovery':[toolchains['arm-none-eabi']],
    'frdmkl26z':[toolchains['arm-none-eabi']],
    'frdmkl27z':[toolchains['arm-none-eabi']],
    'frdmkl28z':[toolchains['arm-none-eabi']],
    'frdmkl43z':[toolchains['arm-none-eabi']],
    'frdmkl81z':[toolchains['arm-none-eabi']],
    'frdmkl82z':[toolchains['arm-none-eabi']],
    'gd32f307c-eval':[toolchains['arm-none-eabi']],
    'gd32f350r-eval':[toolchains['arm-none-eabi']],
    'gd32f450z-eval':[toolchains['arm-none-eabi']],
    'hc32l136k8ta':[toolchains['arm-none-eabi']],
    'hk32f103rb_evb':[toolchains['arm-none-eabi']],
    'hr8p287fjlt':[toolchains['arm-none-eabi']],
    'hr8p296fllt':[toolchains['arm-none-eabi']],
    'hobbit1_evb':[toolchains['csky-abiv2']],
    'imx6dq':[toolchains['arm-none-eabi']],
    'imx6sl':[toolchains['arm-none-eabi']],
    'dh5021a_evb':[toolchains['csky-abiv2']],
    'cb2201':[toolchains['csky-abiv2']],
    'lpcxpresso54018':[toolchains['arm-none-eabi']],
    'lpcxpresso54102':[toolchains['arm-none-eabi']],
    'lpcxpresso54114':[toolchains['arm-none-eabi']],
    'lpcxpresso54608':[toolchains['arm-none-eabi']],
    'lpcxpresso54628':[toolchains['arm-none-eabi']],
    'm100c':[toolchains['arm-none-eabi']],
    'm400':[toolchains['arm-none-eabi']],
    'mk1101':[toolchains['arm-none-eabi']],
    'mk3060':[toolchains['arm-none-eabi']],
    'mk3080':[toolchains['arm-none-eabi']],
    'mk3165':[toolchains['arm-none-eabi']],
    'mk3166':[toolchains['arm-none-eabi']],
    'mk3239':[toolchains['arm-none-eabi']],
    'mt7682s':[toolchains['arm-none-eabi']],
    'numaker-pfm-m487':[toolchains['arm-none-eabi']],
    'numaker-pfm-nano130':[toolchains['arm-none-eabi']],
    'nutiny-evb-nano130':[toolchains['arm-none-eabi']],
    'pca10056':[toolchains['arm-none-eabi']],
    'pca10040':[toolchains['arm-none-eabi']],
    'pca10040e':[toolchains['arm-none-eabi']],
    'saml21_iot_sk':[toolchains['arm-none-eabi']],
    'ssc1667':[toolchains['arm-none-eabi']],
    'starterkit':[toolchains['arm-none-eabi']],
    'stm32f091rc-nucleo':[toolchains['arm-none-eabi']],
    'stm32f103rb-nucleo':[toolchains['arm-none-eabi']],
    'stm32f401re-nucleo':[toolchains['arm-none-eabi']],
    'stm32f411re-nucleo':[toolchains['arm-none-eabi']],
    'stm32f412zg-nucleo':[toolchains['arm-none-eabi']],
    'stm32f429zi-nucleo':[toolchains['arm-none-eabi']],
    'stm32f769i-discovery':[toolchains['arm-none-eabi']],
    'stm32l073rz-nucleo':[toolchains['arm-none-eabi']],
    'stm32l432kc-nucleo':[toolchains['arm-none-eabi']],
    'stm32l433rc-nucleo':[toolchains['arm-none-eabi']],
    'stm32l476rg-nucleo':[toolchains['arm-none-eabi']],
    'stm32l496g-discovery':[toolchains['arm-none-eabi']],
    'sv6266_evb':[toolchains['nds32le-elf-newlib-v3']],
    'msp432p4111launchpad':[toolchains['arm-none-eabi']],
    'xr871evb':[toolchains['arm-none-eabi']],
    'rk1108':[toolchains['arm-rockchip-linux-gnueabihf']],
    'uno-91h':[toolchains['arm-none-eabi']],
    'xr809':[toolchains['arm-none-eabi']],
    'wm_w600_kit':[toolchains['arm-none-eabi']],
    'xm510_evb':[toolchains['arm-none-eabi']],
}
