from setuptools import setup

dependencies = [
    "aiofiles==0.7.0",  # Async IO for files
    "blspy==1.0.13",  # Signature library
    "chiavdf==1.0.6",  # timelord and vdf verification
    "chiabip158==1.1",  # bip158-style wallet filters
    "chiapos==1.0.10",  # proof of space
    "clvm==0.9.7",
    "clvm_tools==0.4.5",  # Currying, Program.to, other conveniences
    "chia_rs==0.1.5",
    "clvm-tools-rs==0.1.19",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.8.1",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.5",  # Colorizes terminal output
    "colorlog==6.6.0",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==36.0.2",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.7.1",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.6.0",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.2.3",  # Gives the moon processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    # TODO: when moving to click 8 remove the pinning of black noted below
    "click==7.1.2",  # For the CLI
    "dnspython==2.2.0",  # Query DNS seeds
    "watchdog==2.1.9",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.17",  # dns lib
    "typing-extensions==4.3.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.0.4",
    "packaging==21.3",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    "coverage",
    "pre-commit",
    "py3createtorrent",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy",
    # TODO: black 22.1.0 requires click>=8, remove this pin after updating to click 8
    "black==21.12b0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.0",
    "types-aiofiles",
    "types-click~=7.1",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

kwargs = dict(
    name="moon-blockchain",
    author="Mariano Sorgente",
    author_email="root@mooncoin.top",
    description="Moon blockchain full node, farmer, timelord, and wallet.",
    url="https://mooncoin.top/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="moon blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "moon",
        "moon.cmds",
        "moon.clvm",
        "moon.consensus",
        "moon.daemon",
        "moon.data_layer",
        "moon.full_node",
        "moon.timelord",
        "moon.farmer",
        "moon.harvester",
        "moon.introducer",
        "moon.plot_sync",
        "moon.plotters",
        "moon.plotting",
        "moon.pools",
        "moon.protocols",
        "moon.rpc",
        "moon.seeder",
        "moon.server",
        "moon.simulator",
        "moon.types.blockchain_format",
        "moon.types",
        "moon.util",
        "moon.wallet",
        "moon.wallet.db_wallet",
        "moon.wallet.puzzles",
        "moon.wallet.rl_wallet",
        "moon.wallet.cat_wallet",
        "moon.wallet.did_wallet",
        "moon.wallet.nft_wallet",
        "moon.wallet.settings",
        "moon.wallet.trading",
        "moon.wallet.util",
        "moon.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "moon = moon.cmds.moon:main",
            "moon_daemon = moon.daemon.server:main",
            "moon_wallet = moon.server.start_wallet:main",
            "moon_full_node = moon.server.start_full_node:main",
            "moon_harvester = moon.server.start_harvester:main",
            "moon_farmer = moon.server.start_farmer:main",
            "moon_introducer = moon.server.start_introducer:main",
            "moon_crawler = moon.seeder.start_crawler:main",
            "moon_seeder = moon.seeder.dns_server:main",
            "moon_timelord = moon.server.start_timelord:main",
            "moon_timelord_launcher = moon.timelord.timelord_launcher:main",
            "moon_full_node_simulator = moon.simulator.start_simulator:main",
            "moon_data_layer = moon.server.start_data_layer:main",
            "moon_data_layer_http = moon.data_layer.data_layer_server:main",
        ]
    },
    package_data={
        "moon": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "moon.util": ["initial-*.yaml", "english.txt"],
        "moon.ssl": ["moon_ca.crt", "moon_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/MOONCOINTEAM/moon-blockchain/",
        "Changelog": "https://github.com/MOONCOINTEAM/moon-blockchain/blob/main/CHANGELOG.md",
    },
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
