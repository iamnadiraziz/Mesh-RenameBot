class EnTrans:
    
    WRONG_VALUE_ERROR = "Invalid value entered for {} variable."
    
    START_MSG = "Salam, bu mənəm! DPB Rename Bot. Sadəcə faylı göndər!"
     
    CANCEL_MESSAGE = "Bu yükləmə ləğv oldundu."
    
    RENAME_NO_FILTER_MATCH = "HEÇ BİR FİLTER UYĞUN GƏLMƏDİ \nUsing Ad dəyişmək üçün istifadə edin. Əgər ad seçilməyibsə, /filters komandasından istifadə edə bilərsiniz."

    RENAME_FILTER_MATCH_USED = "Dəyişmək üçün filterlərdən istifadə edin. Əgər ad seçməmisinizsə, /filters komandasından istifadə edə bilərsiniz"

    RENAME_NOFLTR_NONAME = "Adı bu formatda daxil edin :- ```/rename yeni fayl adı.uzantı``` və ya ```Bəzi filterləri əldə etmək üçün /filters istifadə edin```"

    RENAME_CANCEL = "Əməliyyatı ləğv et."

    RENAMING_FILE = "Faylıən adı dəyişdirilir..."
    
    DL_RENAMING_FILE = "Fayl yüklənməsi..."

    RENAME_ERRORED_REPORT = "Yükləmə alınmadı."

    RENAME_CANCEL_BY_USER = "İstifadəçi tərəfindən ləğv olundu."

    FLTR_ADD_LEFT_STR = "Filter əlavə olunur: <code>{}</code> <code>To Left</code>"
    FLTR_ADD_RIGHT_STR = "Filter əlavə olunur: <code>{}</code> <code>To Right</code>"
    FLTR_RM_STR = "Filteri sil: <code>{}</code>"
    FLTR_REPLACE_STR = "Filteri dəyiş: <code>{}</code> with <code>{}</code>"

    CURRENT_FLTRS = "Hal-hazırda olan filterləriniz:-"
    ADD_FLTR = "Filter əlavə et."
    RM_FLTR = "Filteri sil."

    FILTERS_INTRO = """
Welcome to adding filter.
3 Types of filter.

Replace Filter:- This filter will replace a
given word with the one you sepcified

Addition Filter:- This filter will add given word
at end or beginning.

Remove Filter:- This filer will remove given word
from the while file name.

"""

    ADD_REPLACE_FLTR = "Add Replace Filter."
    ADD_ADDITION_FLTR = "Add Addition Filter."
    ADD_REMOVE_FLTR = "Add Remove Filter."
    BACK = "Back."

    REPALCE_FILTER_INIT_MSG = "Send the msg in this format. <code>what to replace | what to replace with</code> or /ignore to go back.\nNote that sapce after and before '|' will be considered."

    NO_INPUT_FROM_USER = "No input received from you."
    INPUT_IGNORE = "Received ignore from you."
    WRONG_INPUT_FORMAT = "The input is not valid. Check the format which is given."
    REPLACE_FILTER_SUCCESS = "Added the Replace filter successfully. <code>'{}'</code> will be replaced with <code>'{}'</code>."

    ADDITION_FILTER_INIT_MSG = "Enter the text that you want to add or /ignore to go back."

    ADDITION_FILTER_SUCCESS_LEFT = "Added the Addition filter successfully. <code>{}</code> will be added to <code>LEFT</code>."

    ADDITION_FILTER_SUCCESS_RIGHT = "Added the Addition filter successfully. <code>{}</code> will be added to <code>RIGHT</code>."

    ADDITION_LEFT = "Addition to LEFT."
    ADDITION_RIGHT = "Addition to RIGHT."

    ADDITION_POSITION_PROMPT = "Where do you want to add the text."

    REMOVE_FILTER_INIT_MSG = "Enter the text that you want to remove or /ignore to go back."

    REMOVE_FILTER_SUCCESS = "Added the Remove filter successfully. <code>{}</code> will be removed."

    REPLY_TO_MEDIA = "Reply /rename to a media file."

    HELP_STR = """
`/start` - Check if the bot is running.
`/rename` - Reply to media to rename `/rename filename.extension`. If only `/rename` is used filters will be used.
`/filters` - Add/Remove Filters. Use this command to see what are these.
`/setthumb` - Reply to image to set the thumbnail permanently.
`/getthumb` - Get the thumbnail which is currently set.
`/clrthumb` - Remove the thumbnail which is set.
`/mode` - Change between 3 modes:-
    - Same format as it was sent. [If doc is sent doc is uploaded if video is sent video is uploaded.]
    - Force to Document. [Everything is uploaded as a file.]
    - Upload general media. [In streamable video/audio. etc.]
`/queue` - Gives the state of your rename and the load on bot.
    """
