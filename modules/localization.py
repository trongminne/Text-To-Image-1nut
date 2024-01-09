import json
import os


current_translation = {}
localization_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'language')

def localization_js(filename):
    global current_translation

    if isinstance(filename, str):
        full_name = os.path.abspath(os.path.join(localization_root, filename + '.json'))
        print('Debug: Trying to load file:', full_name)  # Thêm dòng này
        if os.path.exists(full_name):
            try:
               with open(full_name, encoding='utf-8') as f:
                    current_translation = json.load(f)
                    assert isinstance(current_translation, dict)

                    for k, v in current_translation.items():
                        assert isinstance(k, str)
                        assert isinstance(v, str)

                    # Lặp qua từng component và thay thế các trường thông tin bằng phiên bản dịch (nếu có)
                    for c in components:
                        label = getattr(c, 'label', None)
                        value = getattr(c, 'value', None)
                        choices = getattr(c, 'choices', None)
                        info = getattr(c, 'info', None)

                        # Dịch label
                        if label and label in current_translation:
                            translated_label = current_translation[label]
                            setattr(c, 'label', translated_label)
                            print(f"Translated label: {label} -> {translated_label}")

                        # Dịch value
                        if value and value in current_translation:
                            translated_value = current_translation[value]
                            setattr(c, 'value', translated_value)
                            print(f"Translated value: {value} -> {translated_value}")

                        # Dịch choices
                        if choices and isinstance(choices, list):
                            new_choices = []
                            for choice in choices:
                                if choice and choice in current_translation:
                                    translated_choice = current_translation[choice]
                                    new_choices.append(translated_choice)
                                    print(f"Translated choice: {choice} -> {translated_choice}")
                                else:
                                    new_choices.append(choice)
                            setattr(c, 'choices', new_choices)

                        # Dịch info
                        if info and info in current_translation:
                            translated_info = current_translation[info]
                            setattr(c, 'info', translated_info)
                            print(f"Translated info: {info} -> {translated_info}")

                print('Debug: File loaded successfully.')  # Thêm dòng này
            except Exception as e:
                print(str(e))
                print(f'Failed to load localization file {full_name}')
                return  # Thêm dòng này để kết thúc hàm nếu có lỗi

    return f"window.localization = {json.dumps(current_translation)}"


def dump_english_config(components):
    all_texts = []
    for c in components:
        label = getattr(c, 'label', None)
        value = getattr(c, 'value', None)
        choices = getattr(c, 'choices', None)
        info = getattr(c, 'info', None)

        if isinstance(label, str):
            all_texts.append(label)
        if isinstance(value, str):
            all_texts.append(value)
        if isinstance(info, str):
            all_texts.append(info)
        if isinstance(choices, list):
            for x in choices:
                if isinstance(x, str):
                    all_texts.append(x)
                if isinstance(x, tuple):
                    for y in x:
                        if isinstance(y, str):
                            all_texts.append(y)

    config_dict = {k: k for k in all_texts if k != "" and 'progress-container' not in k}
    filename = 'en'
    full_name = os.path.abspath(os.path.join(localization_root, f'{filename}.json'))
    print('path en: ', full_name)
    localization_js(filename)

    with open(full_name, "w", encoding="utf-8") as json_file:
        json.dump(config_dict, json_file, indent=4)

    return
