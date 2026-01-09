from .execution import (
    get_current_step,
    mark_done,
    is_stuck,
    get_logs
)
from .speech_service import synthesize_speech
from .language_service import generate_parent_insight


def ui_get_step():
    # NO speech here
    step = get_current_step()
    return {"step": step}


def ui_done():
    # NO speech here
    next_step = mark_done()
    return {"next_step": next_step}


def ui_check_stuck():
    if is_stuck():
        help_text = "It’s okay. Take your time. Try this step slowly."
        audio = synthesize_speech(help_text)
        return {
            "stuck": True,
            "help": help_text,
            "audio": f"/{audio}"
        }
    return {"stuck": False}


def ui_parent_view():
    insight = generate_parent_insight(get_logs())
    return {"insight": insight}
