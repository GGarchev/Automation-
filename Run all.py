import subprocess
import time
import os

# List of paths to your scripts
scripts = [
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Shortcuts).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Environment).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Slo240).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel RAV).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Reticle).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (BC+).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Zeroing).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Distance).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-0 (Carousel Wi-Fi).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-1 (Video Resolution).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-1 (Video Sens).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-2 (Rec Blend).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-2 (Rec Mic).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-2 (Rec Format).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-2 (Rec RAV).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display  Brightness).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Widgets).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Compass).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Sleep).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Lang).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Reticle Sellection).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Reticle Import).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-3 (Display Reticle Ballistic).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-4 (Profile Current).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-4 (Profile Other).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-4 (Profile Import).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-4 (Profile Export).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-5 (Wireless Mode).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-5 (Wireless Info).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-5 (Wireless Remote).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-5 (Wireless LRF).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-5 (Wireless B-LRF).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-6 (Settings Units).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-6 (Settings Date and Time).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-6 (Settings Device type).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-6 (Settings  Zoom).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\T-6 (Settings Factory Restore).py",
]


def run_script(script_path):
    try:
        # Use subprocess.Popen() to capture both output and errors live
        process = subprocess.Popen(
            ["python", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Set to True to capture output as text
            universal_newlines=True
        )

        # Print and log output in real time
        log_file_path = os.path.join("C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\logs",
                                     f"log_{os.path.basename(script_path)}.txt")

        with open(log_file_path, "w", encoding="utf-8", errors="replace") as log_file:
            log_file.write(f"--- Script: {script_path} ---\n")

            for line in process.stdout:
                print(line, end='')  # Print to console
                log_file.write(line)  # Write to log file
                log_file.flush()  # Ensure the log is updated in real-time

            # Capture and log errors
            stderr_output = process.stderr.read()
            if stderr_output:
                print(f"Errors:\n{stderr_output}")
                log_file.write(f"Errors:\n{stderr_output}")
                log_file.flush()

        process.wait()  # Wait for the process to finish
        print(f"--- Finished running script: {script_path} ---")
        print(f"Return Code: {process.returncode}")

    except Exception as e:
        print(f"An error occurred while running {script_path}: {e}")


def run_all_scripts(scripts, delay=1):
    # Remove empty paths
    valid_scripts = [script for script in scripts if script.strip()]

    # Ensure log directory exists
    os.makedirs("C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\logs", exist_ok=True)

    for i, script in enumerate(valid_scripts):
        print(f"Running script: {script}")
        run_script(script)
        print("\n" + "=" * 40 + "\n")  # Divider for readability between scripts

        # Add a specific delay between "T-0 (Carousel RAV)" and "T-0 (Carousel Reticle)"
        if script.endswith("T-0 (Carousel RAV).py"):
            print("Adding a 10-second delay before running 'T-0 (Carousel RAV).py'")
            time.sleep(2)

        # Optional general delay between all scripts (in seconds)
        time.sleep(delay)


if __name__ == "__main__":
    run_all_scripts(scripts, delay=3)  # Adjust delay if needed
