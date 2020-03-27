import pyperclip
import time
import os

codes = {

    # Informational.
    100: ('continue',),
    101: ('switching_protocols',),
    102: ('processing',),
    103: ('checkpoint',),
    122: ('uri_too_long', 'request_uri_too_long'),
    200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
    201: ('created',),
    202: ('accepted',),
    203: ('non_authoritative_info', 'non_authoritative_information'),
    204: ('no_content',),
    205: ('reset_content', 'reset'),
    206: ('partial_content', 'partial'),
    207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
    208: ('already_reported',),
    226: ('im_used',),

    # Redirection.
    300: ('multiple_choices',),
    301: ('moved_permanently', 'moved', '\\o-'),
    302: ('found',),
    303: ('see_other', 'other'),
    304: ('not_modified',),
    305: ('use_proxy',),
    307: ('temporary_redirect', 'temporary_moved', 'temporary'),
    308: ('permanent_redirect',
          'resume_incomplete', 'resume',),  # These 2 to be removed in 3.0

    # Client Error.
    400: ('bad_request', 'bad'),
    401: ('unauthorized',),
    402: ('payment_required', 'payment'),
    403: ('forbidden',),
    404: ('not_found', '-o-'),
    405: ('method_not_allowed', 'not_allowed'),
    406: ('not_acceptable',),
    407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
    408: ('request_timeout', 'timeout'),
    409: ('conflict',),
    410: ('gone',),
    411: ('length_required',),
    412: ('precondition_failed', 'precondition'),
    413: ('request_entity_too_large',),
    414: ('request_uri_too_large',),
    415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
    416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
    417: ('expectation_failed',),
    421: ('misdirected_request',),
    422: ('unprocessable_entity', 'unprocessable'),
    423: ('locked',),
    424: ('failed_dependency', 'dependency'),
    426: ('upgrade_required', 'upgrade'),
    428: ('precondition_required', 'precondition'),
    429: ('too_many_requests', 'too_many'),
    431: ('header_fields_too_large', 'fields_too_large'),
    451: ('unavailable_for_legal_reasons', 'legal_reasons'),

    # Server Error.
    500: ('internal_server_error', 'server_error', '/o\\', '✗'),
    501: ('not_implemented',),
    502: ('bad_gateway',),
    503: ('service_unavailable', 'unavailable'),
    504: ('gateway_timeout',),
    505: ('http_version_not_supported', 'http_version'),
    506: ('variant_also_negotiates',),
    507: ('insufficient_storage',),
    510: ('not_extended',),
    511: ('network_authentication_required', 'network_auth', 'network_authentication'),
}


def display_welcome():
    print("|---------------------------------------------|")
    print("| ~~ @highpolarbear's Htaccess generator. ~~  |")
    print("|if you have a common file for all your errors|")
    print("|on your apache server, this generates most of|")
    print("|the error codes.                             |")
    print("|---------------------------------------------|\n")


def display_menu():
    print(" == Menu. ==\n")
    print("1. Generate htacess codes.")
    print("2. View library of codes.")
    print("0. View Menu.")
    print("C. Exit")
    menu_option_input = input("> ")

    if(menu_option_input == "C" or menu_option_input == "c"):
        print("bye !")
        exit()

    return menu_option_input


display_welcome()
menu_option = display_menu()

while (menu_option != "C" or menu_option != "c"):

    if (menu_option == "1"):

        print("write your general html file name (or full path) to generate htaccess.")
        general_file_name = input("> ")

        output = ""

        for code in codes:
            output += "ErrorDocument " + \
                str(code) + " /" + str(general_file_name)
            output += "\n"

        pyperclip.copy(output)
        print(" \n Generated ! It begins like this :")
        print(output[0:100] + "...  \n")
        print("Your output has been copied to your clipboard. \n")
        menu_option = display_menu()

    elif (menu_option == "2"):
        for x in codes:
            print(str(x) + " : " + str(codes[x]))

        menu_option = display_menu()

    elif (menu_option == "clear"):
        os.system("clear")
        menu_option = display_menu()

    elif (menu_option == "cls"):
        os.system("cls")
        menu_option = display_menu()

    else:
        if (menu_option == "0"):
            try:
                os.system("clear")
            except:
                os.system("cls")

            display_welcome()
            menu_option = display_menu()

        else:
            print("\n!!! Wrong option inputted. !!!\n")
            menu_option = display_menu()
