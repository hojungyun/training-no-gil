import psutil
import curses

"""HOW TO RUN:
poetry run python <path_to_your_script>
"""


def display_cpu_usage_chart(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(1000)  # Refresh every second

    while True:
        stdscr.clear()  # Clear the screen

        # Display title
        stdscr.addstr(0, 0, "Real-Time CPU Usage (Bar Chart)", curses.A_BOLD)
        stdscr.addstr(1, 0, f"{'CPU Core':<10}{'Usage (%)':<10}{'Chart'}")
        stdscr.addstr(2, 0, "-" * 30)

        # Fetch CPU usage per core
        cpu_percentages = psutil.cpu_percent(percpu=True)

        # Display bar chart for each core
        for i, percentage in enumerate(cpu_percentages):
            bar_length = int(percentage // 2)  # Length of the bar, 1 "#" represents 2% usage
            bar = "#" * bar_length  # Create the bar

            # Display core usage and the corresponding bar
            stdscr.addstr(3 + i, 0, f"Core {i + 1:<7}{percentage:<10.1f}{bar}")

        # Display total CPU usage
        total_cpu = psutil.cpu_percent()
        stdscr.addstr(3 + len(cpu_percentages), 0, "-" * 30)
        stdscr.addstr(4 + len(cpu_percentages), 0, f"Total CPU: {total_cpu:.1f}%")

        # Handle user input for exit (press 'q' to quit)
        key = stdscr.getch()
        if key == ord('q'):
            break

        stdscr.refresh()  # Refresh the screen


if __name__ == "__main__":
    curses.wrapper(display_cpu_usage_chart)
