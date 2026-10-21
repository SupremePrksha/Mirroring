import os
import sys
import time
import random
import shutil
import subprocess
from datetime import datetime


# ------------------------------------------------------------
# First, make sure the Python stuff we need is installed.
# ------------------------------------------------------------

def check_python_packages():
    packages = ["rich"]
    missing = []

    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)

    if not missing:
        return

    print()
    print("==============================================")
    print("        ULTRON // DEPENDENCY CHECK")
    print("==============================================")
    print()

    for package in missing:
        print(f"[+] Installing missing package: {package}")

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package
        ])

        print(f"[+] {package} installed.")

    print()
    print("[+] All Python dependencies are ready.")
    print("[+] Restarting ULTRON...")
    time.sleep(1)

    os.execv(sys.executable, [sys.executable] + sys.argv)


check_python_packages()


# ------------------------------------------------------------
# Rich is safe to import now.
# ------------------------------------------------------------

from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.align import Align
from rich.text import Text
from rich.table import Table
from rich.tree import Tree
from rich.live import Live


console = Console()

TARGET_IP = "192.168.43.1"
VERSION = "ULTRON // NEURAL MIRROR CORE 10.0"


# ------------------------------------------------------------
# Basic terminal functions
# ------------------------------------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def set_terminal_title():
    if os.name == "nt":
        os.system("title ULTRON // NEURAL MIRROR CORE")


def slow_print(text, style="white", delay=0.012):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)

    console.print()


def random_matrix_line(length=65):
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%<>[]{}"
    return "".join(random.choice(chars) for _ in range(length))


# ------------------------------------------------------------
# Check ADB and scrcpy.
# These are system programs, so we don't install them with pip.
# ------------------------------------------------------------

def check_system_programs():

    missing = []

    if shutil.which("adb") is None:
        missing.append("ADB")

    if shutil.which("scrcpy") is None:
        missing.append("scrcpy")

    if not missing:
        return True

    clear_screen()

    message = (
        "[bold red]ULTRON // SYSTEM DEPENDENCY FAILURE[/bold red]\n\n"
        "The following system programs were not found:\n\n"
    )

    for item in missing:
        message += f"[bold yellow]◆ {item}[/bold yellow]\n"

    message += (
        "\n"
        "[dim]These are not Python packages.[/dim]\n"
        "[dim]Install them once, then launch ULTRON again.[/dim]"
    )

    console.print(
        Panel(
            message,
            border_style="bright_red",
            padding=1
        )
    )

    input("\nPress Enter to exit...")
    return False


# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

def show_header():

    clear_screen()

    current_time = datetime.now().strftime("%I:%M:%S %p")

    title = Text()
    title.append("◢ ", style="bright_red")
    title.append("ULTRON", style="bold bright_red")
    title.append(" // ", style="bright_white")
    title.append("NEURAL MIRROR", style="bold bright_cyan")
    title.append(" ◣", style="bright_red")

    subtitle = Text(
        "AUTONOMOUS TERMINAL CONTROL INTERFACE",
        style="bold bright_magenta"
    )

    status = Text()
    status.append("● ", style="bright_green")
    status.append("CORE ONLINE", style="bold green")
    status.append("    ")
    status.append(current_time, style="bold cyan")
    status.append("    ")
    status.append("SECURE", style="bold green")

    content = Group(
        Align.center(title),
        Align.center(subtitle),
        Text(""),
        Align.center(status)
    )

    console.print(
        Panel(
            content,
            border_style="bright_red",
            padding=(1, 2)
        )
    )


# ------------------------------------------------------------
# Boot animation
# ------------------------------------------------------------

def boot_sequence():

    clear_screen()

    console.print(
        Align.center(
            Text(
                "\n◢ ULTRON NEURAL CORE ◣",
                style="bold bright_red"
            )
        )
    )

    console.print(
        Align.center(
            Text(
                "INITIALIZING TERMINAL...",
                style="bright_cyan"
            )
        )
    )

    time.sleep(0.5)

    tasks = [
        "Loading neural interface",
        "Checking terminal matrix",
        "Scanning ADB subsystem",
        "Synchronizing wireless protocols",
        "Calibrating video engine",
        "Loading mirror subsystem",
        "Establishing secure channel",
        "Activating ULTRON core"
    ]

    for task in tasks:

        with console.status(
            f"[bold cyan]◆ {task}...",
            spinner="dots12"
        ):
            time.sleep(random.uniform(0.12, 0.3))

        console.print(
            f"[bold green]  ✓[/bold green] {task}"
        )

    console.print()

    for _ in range(3):
        console.print(
            random_matrix_line(random.randint(45, 75)),
            style="dim red"
        )
        time.sleep(0.04)

    console.print()

    console.print(
        Panel(
            "[bold bright_red]ULTRON CORE ONLINE[/bold bright_red]\n"
            "[bright_cyan]Neural interface synchronized.[/bright_cyan]\n"
            "[dim]Operator control available.[/dim]",
            border_style="bright_red",
            padding=1
        )
    )

    time.sleep(1)


# ------------------------------------------------------------
# Resolution selector
# ------------------------------------------------------------

def choose_resolution():

    clear_screen()

    console.print(
        Panel(
            Align.center(
                Text(
                    "◢ VISUAL RESOLUTION MATRIX ◣",
                    style="bold bright_red"
                )
            ),
            border_style="bright_red"
        )
    )

    table = Table(
        title="VIDEO ENGINE PROFILES",
        border_style="bright_cyan"
    )

    table.add_column("KEY", justify="center", style="bold cyan")
    table.add_column("QUALITY", justify="center", style="bold white")
    table.add_column("BITRATE", justify="center", style="bold yellow")
    table.add_column("FPS", justify="center", style="bold green")
    table.add_column("PROFILE")

    table.add_row(
        "1",
        "480p",
        "4 Mbps",
        "60",
        "SMOOTH / LOW LOAD"
    )

    table.add_row(
        "2",
        "720p",
        "8 Mbps",
        "60",
        "HIGH QUALITY / HIGH LOAD"
    )

    console.print(table)
    console.print()

    console.print(
        Panel(
            "[bold yellow]⚠ HIGH QUALITY WARNING[/bold yellow]\n\n"
            "720p gives you a sharper image, but it needs\n"
            "more processing power and network bandwidth.\n\n"
            "[bold red]Possible effects:[/bold red]\n"
            "• Higher CPU/GPU usage\n"
            "• Increased network usage\n"
            "• More latency\n"
            "• Stuttering on weaker connections\n\n"
            "[bold green]480p[/bold green] is recommended when smoothness\n"
            "is more important than image quality.",
            border_style="yellow",
            padding=1
        )
    )

    choice = Prompt.ask(
        "\nSelect visual profile",
        choices=["1", "2"],
        default="1"
    )

    if choice == "1":
        return {
            "name": "SMOOTH 480P",
            "size": "480",
            "bitrate": "4M"
        }

    console.print()

    if not Confirm.ask(
        "[bold yellow]Continue with HIGH QUALITY 720p?[/bold yellow]",
        default=True
    ):
        return {
            "name": "SMOOTH 480P",
            "size": "480",
            "bitrate": "4M"
        }

    return {
        "name": "HIGH QUALITY 720P",
        "size": "720",
        "bitrate": "8M"
    }


# ------------------------------------------------------------
# Diagnostics
# ------------------------------------------------------------

def show_diagnostics():

    show_header()

    tree = Tree(
        "[bold bright_red]◢ ULTRON SYSTEM DIAGNOSTICS ◣"
    )

    core = tree.add("[bold cyan]NEURAL CORE[/bold cyan]")
    core.add("[green]● ONLINE[/green]")
    core.add("[green]● TERMINAL ACTIVE[/green]")
    core.add("[green]● COMMAND SYSTEM READY[/green]")

    adb = tree.add("[bold cyan]ADB SUBSYSTEM[/bold cyan]")
    adb.add("[green]● ADB AVAILABLE[/green]")
    adb.add("[cyan]TCP PORT: 5555[/cyan]")
    adb.add("[yellow]USB DEBUGGING REQUIRED[/yellow]")

    video = tree.add("[bold cyan]VIDEO ENGINE[/bold cyan]")
    video.add("[green]H.264[/green]")
    video.add("[green]60 FPS[/green]")
    video.add("[cyan]480p SMOOTH PROFILE[/cyan]")
    video.add("[magenta]720p HIGH QUALITY PROFILE[/magenta]")

    console.print(
        Panel(
            tree,
            border_style="bright_red",
            padding=1
        )
    )

    console.print()

    shortcuts = Table(
        title="◢ SCRCPY CONTROL MATRIX ◣",
        border_style="bright_magenta"
    )

    shortcuts.add_column(
        "INPUT",
        style="bold cyan",
        justify="center"
    )

    shortcuts.add_column(
        "FUNCTION",
        style="white"
    )

    shortcuts.add_row("Alt + O", "Turn phone screen off")
    shortcuts.add_row("Alt + F", "Toggle fullscreen")
    shortcuts.add_row("Alt + P", "Power button")
    shortcuts.add_row("Right Click", "Back")
    shortcuts.add_row("Middle Click", "Home")

    console.print(shortcuts)

    input("\nPress Enter to return to ULTRON...")


# ------------------------------------------------------------
# Living terminal
# ------------------------------------------------------------

def living_terminal():

    clear_screen()

    start_time = time.time()

    with Live(console=console, refresh_per_second=12) as live:

        for frame in range(80):

            uptime = time.time() - start_time

            neural_load = random.randint(70, 99)
            signal = random.randint(88, 100)
            cpu = random.randint(8, 35)

            table = Table(
                show_header=False,
                box=None,
                expand=True
            )

            table.add_column(width=18)
            table.add_column()
            table.add_column(
                justify="right",
                width=20
            )

            table.add_row(
                "[bold cyan]CORE[/bold cyan]",
                "ULTRON NEURAL ENGINE",
                "[green]ONLINE[/green]"
            )

            table.add_row(
                "[bold cyan]NEURAL LOAD[/bold cyan]",
                f"[bright_magenta]{neural_load}%[/bright_magenta]",
                "STABLE"
            )

            table.add_row(
                "[bold cyan]SIGNAL[/bold cyan]",
                f"[bright_green]{signal}%[/bright_green]",
                "LOCKED"
            )

            table.add_row(
                "[bold cyan]CPU ACTIVITY[/bold cyan]",
                f"{cpu}%",
                "NORMAL"
            )

            table.add_row(
                "[bold cyan]UPTIME[/bold cyan]",
                f"{uptime:06.2f}s",
                "ACTIVE"
            )

            logs = [
                "Monitoring wireless neural bridge...",
                "Scanning ADB endpoint...",
                "Video pipeline synchronized.",
                "Mirror subsystem standing by.",
                "Awaiting operator command...",
                "Neural link stable.",
                "Monitoring signal integrity...",
            ]

            log = logs[frame % len(logs)]

            content = Group(
                Align.center(
                    Text(
                        "◢ ULTRON // LIVE TERMINAL ◣",
                        style="bold bright_red"
                    )
                ),
                Text(""),
                table,
                Text(""),
                Align.center(
                    Text(
                        f"◆ {log}",
                        style="bright_cyan"
                    )
                )
            )

            live.update(
                Panel(
                    content,
                    border_style="bright_red",
                    padding=(1, 2)
                )
            )

            time.sleep(0.08)


# ------------------------------------------------------------
# Wireless connection
# ------------------------------------------------------------

def start_connection():

    if not check_system_programs():
        return

    profile = choose_resolution()

    show_header()

    console.print(
        Panel(
            f"[bold cyan]VIDEO PROFILE[/bold cyan]\n\n"
            f"Mode       : [bold green]{profile['name']}[/bold green]\n"
            f"Resolution: [bold white]{profile['size']}p[/bold white]\n"
            f"Bitrate    : [bold yellow]{profile['bitrate']}[/bold yellow]\n"
            f"Frame rate : [bold green]60 FPS[/bold green]\n"
            f"Codec      : [bold cyan]H.264[/bold cyan]",
            border_style="bright_cyan"
        )
    )

    console.print()

    instructions = Table(
        title="◢ WIRELESS HANDSHAKE PROTOCOL ◣",
        title_style="bold bright_red",
        border_style="bright_cyan"
    )

    instructions.add_column(
        "STEP",
        style="bold bright_magenta",
        justify="center"
    )

    instructions.add_column(
        "ACTION",
        style="white"
    )

    instructions.add_row(
        "01",
        "Enable phone Hotspot or connect both devices to the same Wi-Fi."
    )

    instructions.add_row(
        "02",
        "Make sure the laptop is connected to that network."
    )

    instructions.add_row(
        "03",
        "For a fresh connection, connect the phone through USB."
    )

    console.print(instructions)

    console.print()

    console.print(
        "[bold green][S][/bold green] QUICK CONNECT"
    )

    console.print(
        "[bold cyan][C][/bold cyan] COMPLETE FRESH CONNECTION"
    )

    console.print(
        "[bold red][B][/bold red] BACK"
    )

    choice = Prompt.ask(
        "\nSelect system vector",
        choices=["s", "c", "b"],
        default="c"
    ).lower()

    if choice == "b":
        return

    target_ip = TARGET_IP

    # Fresh USB -> TCP/IP setup
    if choice == "c":

        show_header()

        with Progress(
            SpinnerColumn("dots12"),
            TextColumn(
                "[progress.description]{task.description}"
            ),
            transient=True
        ) as progress:

            progress.add_task(
                description="Resetting ADB connection...",
                total=None
            )

            subprocess.run(
                ["adb", "kill-server"],
                capture_output=True
            )

            subprocess.run(
                ["adb", "start-server"],
                capture_output=True
            )

            time.sleep(0.5)

            progress.add_task(
                description="Searching for phone network address...",
                total=None
            )

            try:

                result = subprocess.run(
                    [
                        "adb",
                        "-d",
                        "shell",
                        "ip",
                        "route"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                if result.returncode != 0:
                    raise RuntimeError("ADB device unavailable")

                found_ip = False

                for line in result.stdout.splitlines():

                    if "src" in line:

                        parts = line.split()

                        if "src" in parts:

                            index = parts.index("src")

                            if index + 1 < len(parts):

                                target_ip = parts[index + 1]
                                found_ip = True
                                break

                if not found_ip:
                    raise RuntimeError(
                        "Could not detect phone IP"
                    )

                console.print(
                    f"\n[bold green]"
                    f"✓ Phone detected: {target_ip}"
                    f"[/bold green]"
                )

            except Exception:

                console.print(
                    Panel(
                        "[bold red]USB CONNECTION FAILED[/bold red]\n\n"
                        "ULTRON could not communicate with the phone.\n\n"
                        "[bold yellow]Check:[/bold yellow]\n"
                        "• USB cable\n"
                        "• USB debugging\n"
                        "• Phone unlocked\n"
                        "• File Transfer mode\n"
                        "• Android debugging permission",
                        border_style="red"
                    )
                )

                target_ip = Prompt.ask(
                    "\nEnter phone IP manually",
                    default=TARGET_IP
                )

        console.print(
            "\n[bold cyan]Activating wireless ADB...[/bold cyan]"
        )

        result = subprocess.run(
            [
                "adb",
                "-d",
                "tcpip",
                "5555"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            console.print(
                Panel(
                    "[bold bright_green]"
                    "WIRELESS ADB READY"
                    "[/bold bright_green]\n\n"
                    "Disconnect the USB cable now.\n"
                    "Then press ENTER.",
                    border_style="bright_green"
                )
            )

            input()

        else:

            console.print(
                "[bold red]"
                "Failed to switch ADB into TCP mode."
                "[/bold red]"
            )

            input("\nPress Enter...")
            return

    # Quick connection
    elif choice == "s":

        show_header()

        target_ip = Prompt.ask(
            "Enter phone IP",
            default=TARGET_IP
        )

    # --------------------------------------------------------
    # Final wireless connection
    # --------------------------------------------------------

    show_header()

    console.print(
        Panel(
            f"[bold cyan]TARGET[/bold cyan]\n"
            f"{target_ip}:5555\n\n"
            "[bold yellow]"
            "ESTABLISHING NEURAL BRIDGE..."
            "[/bold yellow]",
            border_style="bright_cyan"
        )
    )

    with Progress(
        SpinnerColumn("dots12"),
        TextColumn(
            "[progress.description]{task.description}"
        ),
        transient=True
    ) as progress:

        progress.add_task(
            description=f"Connecting to {target_ip}:5555...",
            total=None
        )

        result = subprocess.run(
            [
                "adb",
                "connect",
                f"{target_ip}:5555"
            ],
            capture_output=True,
            text=True
        )

        time.sleep(0.8)

    output = (
        result.stdout + result.stderr
    ).lower()

    if "connected" not in output:

        console.print(
            Panel(
                "[bold red]NETWORK REFUSAL[/bold red]\n\n"
                "The phone rejected the wireless ADB connection.\n\n"
                "[bold yellow]Check:[/bold yellow]\n"
                "• Same Wi-Fi / Hotspot\n"
                "• Correct IP address\n"
                "• USB debugging\n"
                "• Port 5555\n"
                "• Restart the connection process",
                border_style="red"
            )
        )

        input("\nPress Enter...")
        return

    # --------------------------------------------------------
    # Connection successful
    # --------------------------------------------------------

    console.print(
        Panel(
            "[bold bright_green]"
            "✓ NEURAL LINK ESTABLISHED"
            "[/bold bright_green]\n\n"
            f"Target      : {target_ip}:5555\n"
            f"Video       : {profile['name']}\n"
            f"Resolution  : {profile['size']}p\n"
            f"Bitrate     : {profile['bitrate']}\n"
            f"Frame rate  : 60 FPS\n"
            f"Codec       : H.264",
            title="ULTRON // CONNECTION SECURED",
            border_style="bright_green"
        )
    )

    time.sleep(1)

    # --------------------------------------------------------
    # Start scrcpy
    # --------------------------------------------------------

    console.print(
        "\n[bold bright_red]"
        "◢ ACTIVATING VISUAL MIRROR ENGINE ◣"
        "[/bold bright_red]"
    )

    time.sleep(0.8)

    scrcpy_command = [
        "scrcpy",
        "-e",
        "--video-codec=h264",
        f"--video-bit-rate={profile['bitrate']}",
        "--max-fps=60",
        f"--max-size={profile['size']}",
        "--window-title",
        f"ULTRON // {profile['name']}"
    ]

    subprocess.run(scrcpy_command)

    console.print(
        "\n[bold cyan]"
        "Mirror session ended."
        "[/bold cyan]"
    )

    input("\nPress Enter to return to ULTRON...")


# ------------------------------------------------------------
# Main menu
# ------------------------------------------------------------

def main():

    set_terminal_title()

    boot_sequence()

    while True:

        show_header()

        menu = Table(
            show_header=False,
            box=None,
            expand=True
        )

        menu.add_column(
            "KEY",
            style="bold bright_red",
            justify="center",
            width=8
        )

        menu.add_column(
            "SYSTEM VECTOR",
            style="bold white"
        )

        menu.add_row(
            "01",
            "LAUNCH NEURAL MIRROR"
        )

        menu.add_row(
            "02",
            "SYSTEM DIAGNOSTICS"
        )

        menu.add_row(
            "03",
            "LIVE ULTRON TERMINAL"
        )

        menu.add_row(
            "04",
            "SHUTDOWN CORE"
        )

        console.print(
            Panel(
                menu,
                title="[bold bright_red]◢ COMMAND MATRIX ◣[/bold bright_red]",
                border_style="bright_cyan",
                padding=1
            )
        )

        console.print()

        choice = Prompt.ask(
            "[bold cyan]ULTRON AWAITING COMMAND[/bold cyan]",
            choices=["1", "2", "3", "4"],
            default="1"
        )

        if choice == "1":
            start_connection()

        elif choice == "2":
            show_diagnostics()

        elif choice == "3":
            living_terminal()

        elif choice == "4":

            clear_screen()

            console.print(
                Align.center(
                    Text(
                        "\n◢ ULTRON CORE SHUTDOWN ◣",
                        style="bold bright_red"
                    )
                )
            )

            messages = [
                "Closing neural interface...",
                "Disconnecting visual matrix...",
                "Terminating wireless bridge...",
                "Saving terminal state..."
            ]

            for message in messages:

                console.print(
                    f"[dim cyan]◆ {message}[/dim cyan]"
                )

                time.sleep(0.25)

            console.print()

            console.print(
                "[bold bright_red]"
                "ULTRON OFFLINE."
                "[/bold bright_red]"
            )

            time.sleep(1)

            clear_screen()
            sys.exit(0)


# ------------------------------------------------------------
# Start
# ------------------------------------------------------------

if __name__ == "__main__":

    try:

        if not check_system_programs():
            sys.exit(1)

        main()

    except KeyboardInterrupt:

        clear_screen()

        console.print(
            "\n[bold red]"
            "◆ ULTRON CORE INTERRUPTED"
            "[/bold red]"
        )

        console.print(
            "[dim]Terminal session terminated by operator.[/dim]"
        )

        sys.exit(0)