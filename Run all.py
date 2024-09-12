import subprocess
import time
import os

# List of paths to your scripts
scripts = [
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
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-11 (Profile Current).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-12 (Profile Other).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-13 (Profile Import).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-14 (Profile Export).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-6 (Wireless Mode).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-7 (Wireless Info).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-8 (Wireless Remote).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-9 (Wireless LRF).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-10 (Wireless B-LRF).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-3 (Settings Units).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-4 (Settings Date and Time).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-2 (Settings Device type).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-1 (Settings  Zoom).py",
    "C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\Test-5 (Settings Factory Restore).py",
]


def run_script(script_path):
    try:
        # Run the script using subprocess and wait for it to finish
        result = subprocess.run(["python", script_path], capture_output=True, text=True)

        # Print script output and errors
        print(f"\n--- Finished running script: {script_path} ---")
        print(f"Return Code: {result.returncode}")
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Errors:\n{result.stderr}")

        # Log the output to a file
        log_file = os.path.join("C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\logs",
                                f"log_{os.path.basename(script_path)}.txt")
        with open(log_file, "w") as log:
            log.write(f"--- Script: {script_path} ---\n")
            log.write(f"Return Code: {result.returncode}\n")
            log.write(f"Output:\n{result.stdout}\n")
            if result.stderr:
                log.write(f"Errors:\n{result.stderr}\n")

    except Exception as e:
        print(f"An error occurred while running {script_path}: {e}")


def run_all_scripts(scripts, delay=1):
    # Remove empty paths
    valid_scripts = [script for script in scripts if script.strip()]

    # Ensure log directory exists
    os.makedirs("C:\\Users\\ggarchev\\PycharmProjects\\pythonProject\\Automation\\logs", exist_ok=True)

    for script in valid_scripts:
        print(f"Running script: {script}")
        run_script(script)
        print("\n" + "=" * 40 + "\n")  # Divider for readability between scripts

        # Optional delay between scripts (in seconds)
        time.sleep(delay)


if __name__ == "__main__":
    run_all_scripts(scripts, delay=1)  # Adjust delay if needed
