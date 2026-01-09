import time

# ----------------------------
# In-memory execution state
# ----------------------------

steps = []
current_step_index = 0
step_start_time = None
step_logs = []

STUCK_THRESHOLD = 10  # seconds


# ----------------------------
# Setup / Reset (APP BEHAVIOR)
# ----------------------------

def setup_steps(new_steps):
    """
    Called when a parent starts a new routine.
    """
    global steps, current_step_index, step_start_time, step_logs

    steps = new_steps
    current_step_index = 0
    step_logs = []
    step_start_time = time.time()


def reset_execution():
    """
    Called when child mode starts fresh.
    """
    global current_step_index, step_start_time, step_logs

    current_step_index = 0
    step_logs = []
    step_start_time = time.time()


# ----------------------------
# Child Execution
# ----------------------------

def get_current_step():
    if not steps:
        return "No routine loaded"
    return steps[current_step_index]


def mark_done():
    global current_step_index, step_start_time

    if not steps:
        return "No routine loaded"

    now = time.time()
    step_logs.append({
        "step": steps[current_step_index],
        "time_taken": round(now - step_start_time, 2)
    })

    if current_step_index < len(steps) - 1:
        current_step_index += 1
        step_start_time = time.time()
        return steps[current_step_index]

    # End of routine
    return "Routine completed 🎉"


def is_stuck():
    if not step_start_time or not steps:
        return False
    return (time.time() - step_start_time) > STUCK_THRESHOLD


# ----------------------------
# Parent Insights
# ----------------------------

def get_logs():
    return step_logs
