import yt_dlp
import os
import platform
import sys
from pathlib import Path

# UI Libraries
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn
    from rich.layout import Layout
    from rich.table import Table
    from rich.live import Live
    from rich.text import Text
    from rich.prompt import Prompt
    from rich.align import Align
except ImportError:
    print("Error: 'rich' library not found. Run: pip install rich")
    sys.exit(1)

console = Console()

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

class StealthLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass 

def make_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="stats", ratio=1),
        Layout(name="console", ratio=2),
    )
    return layout

def update_ui(d, progress, task_id, layout, threads):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 1)
        downloaded = d.get('downloaded_bytes', 0)
        p = (downloaded / total) * 100
        
        progress.update(task_id, description=f"[bold white]HAWK-ENGINE OVERCLOCKED", completed=p)
        
        stats_table = Table(show_header=False, box=None, padding=(0, 1))
        stats_table.add_row("[bold cyan]CORE[/]", f"[white]hawk-engine 1.1[/]")
        stats_table.add_row("[bold yellow]SPEED[/]", f"[bold yellow]{d.get('_speed_str','N/A')}[/]")
        stats_table.add_row("[bold green]ETA[/]", f"[green]{d.get('_eta_str','N/A')}[/]")
        stats_table.add_row("[bold red]ACTIVE[/]", f"[red]{threads} CONNS[/]")
        
        layout["stats"].update(Panel(Align.center(stats_table, vertical="middle"), title="[bold white]Telemetry[/]", border_style="red"))
        
        fname = d.get('filename','').split(os.sep)[-1]
        log_content = (
            f"[bold white]TARGET:[/] [dim]{fname[:30]}...[/]\n"
            f"[bold red]ENGINE:[/] [white]MAX-PARALLEL EXECUTION[/]\n"
            f"[bold magenta]SOCKET:[/] [white]FORCE-SENSITIVE BUFFERS[/]"
        )
        layout["console"].update(Panel(Align.center(log_content, vertical="middle"), title="[bold white]hawk-engine ver. 1.1[/]", border_style="magenta"))

def download_video(url, threads):
    base_dir = Path(__file__).parent
    save_path = base_dir / "site_downloads"
    save_path.mkdir(exist_ok=True)
    
    cookie_folder = base_dir / "cookies"
    cookie_path = None
    if cookie_folder.exists():
        for f in cookie_folder.glob("*.txt"):
            if f.stem.lower() in url.lower():
                cookie_path = str(f)
                break
        if not cookie_path:
            all_c = list(cookie_folder.glob("*.txt"))
            cookie_path = str(all_c[0]) if all_c else None

    layout = make_layout()
    layout["header"].update(Panel(Text("📂 PROJECT: DOWNLOAD ME :)", style="bold cyan", justify="center"), border_style="cyan"))

    progress = Progress(
        TextColumn("[bold white]{task.description}"),
        BarColumn(bar_width=None, style="black", complete_style="bright_red"),
        "[progress.percentage]{task.percentage:>3.0f}%",
        DownloadColumn(),
        TransferSpeedColumn(),
        expand=True
    )
    task_id = progress.add_task("Igniting...", total=100)
    layout["footer"].update(Panel(progress, border_style="bright_red"))

    try:
        with Live(layout, refresh_per_second=10, screen=True):
            ydl_opts = {
                'format': 'best',
                'outtmpl': str(save_path / '%(title)s.%(ext)s'),
                'cookiefile': cookie_path,
                'logger': StealthLogger(),
                'concurrent_fragment_downloads': int(threads),
                'buffersize': 8 * 1024 * 1024, # 8MB Buffer for extreme threading
                'retries': 50,
                'nocheckcertificate': True,
                'progress_hooks': [lambda d: update_ui(d, progress, task_id, layout, threads)],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        
        clear_screen()
        console.print(Panel(Align.center("[bold green]✅ EXTRACTION COMPLETE\nHAWK-ENGINE DISENGAGED SUCCESSFULLY[/bold green]"), border_style="green", expand=False))

    except KeyboardInterrupt:
        clear_screen()
        console.print(Panel(Align.center("[bold red]🛑 EMERGENCY SHUTDOWN\nCORE DUMPED[/bold red]"), border_style="red", expand=False))
        sys.exit(0)

if __name__ == "__main__":
    try:
        clear_screen()
        console.print(Align.center(Panel("[bold cyan]PROJECT: DOWNLOAD ME :)[/bold cyan]\n[dim]CORE: hawk-engine ver. 1.1 [OVERCLOCKED][/dim]", border_style="cyan", expand=False)))

        # New Aggressive Selection Table
        table = Table(title="[bold white]NETWORK SATURATION LEVELS[/]", box=None)
        table.add_column("LVL", style="bold cyan")
        table.add_column("THREADS", style="bold magenta")
        table.add_column("TARGET PROFILE", style="white")
        
        table.add_row("1", "32", "Safe - Standard Sites (YouTube, Twitter)")
        table.add_row("2", "128", "Greedy - High-Capacity Servers (Adult Webbies)")
        table.add_row("3", "256", "Violent - Massive CDN Networks (Google Drive, Akamai)")
        table.add_row("4", "512", "God Mode - Data Centers / 1Gbps+ Fiber Only")
        
        console.print(Align.center(Panel(table, border_style="bright_white", padding=(1, 4))))
        
        choice = Prompt.ask("\n[bold red]SELECT INTENSITY (1-4)[/]", choices=["1", "2", "3", "4"], default="2")
        thread_map = {"1": 32, "2": 128, "3": 256, "4": 512}
        
        url = console.input("[bold cyan]TARGET URL[/] [bold red]→[/] ").strip()
        
        if url:
            download_video(url, thread_map[choice])
            
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)