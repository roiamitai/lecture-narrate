#
def slide_extract_lecture_notes (slide)->str:
    return slide.notes_slide.notes_text_frame.text
#