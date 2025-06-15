#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

adwmgui_agreement = """TR:

AdWMGUI kullanım sözleşmesi:

Yazar: LinuxUsersLinuxMint
Sözleşme içeriği: AdWMGUI yazılımının kullanımı içindir.
Oluşturulma tarihi: 6/11/2025 - 22:37
Son düzenlenme tarihi: --/--/---- - --:--

- AdWMGUI kullanım sözleşme açıklaması -

* Bu sözleşme kullanıcıların AdWMGUI yazılımını kullanırken nelere dikkat etmesi gerektiğiyle ilgilidir.

- AdWMGUI nereden indirilmeli? -

* AdWMGUI yazılımı açık kaynaklıdır bu sayede AdWMGUI kaynak koduna erişim sağlayabilir ve kaynak kodu düzenleyebilir güvenilmez düzenlemelerden veya zararlı yazılımlardan korunmak için AdWMGUI yazılımını belirtilen kaynaklardan edinmenizi öneririz:
 * Github: https://github.com/LinuxUsersLinuxMint/AdWMGUI

- AdWMGUI kullanırken dikkat edilmesi gerekenler -

* AdWMGUI yazılımını kullanırken belirtilen sistem gereksinimlerine uyduğunuzdan emin olunuz.
* En iyi kullanıcı deneyimi için AdWMGUI yazılımının daima en güncel sürümünü edininiz ve güncellemeleri belirtilen Github adresinden düzenli olarak kontrol etmeninizi öneririz.

- Kullanıcı sorumlulukları -

* AdWMGUI yazılımındaki özellikleri kullanırken istenmeyen tüm sonuçların sorumluluğu kullanıcıya aittir.

EN:

AdWMGUI usage agreement:

Author: LinuxUsersLinuxMint
Agreement content: For the use of AdWMGUI software.
Created on: 6/11/2025 - 10:37 PM
Last edited: --/--/---- - --:--

- AdWMGUI usage agreement description -

* This agreement is about what users should be aware of when using AdWMGUI software.

- Where to download AdWMGUI? -

* The AdWMGUI software is open source, so you can access and edit the AdWMGUI source code. To protect yourself from unreliable edits or malware, we recommend that you obtain the AdWMGUI software from the sources listed:
 * Github: https://github.com/LinuxUsersLinuxMint/AdWMGUI

- Things to consider when using AdWMGUI -

* Make sure that you comply with the specified system requirements when using the AdWMGUI software.
* For the best user experience, we recommend that you always obtain the latest version of AdWMGUI and regularly check for updates at the specified Github address.

- User responsibilities -

* The user is responsible for all unintended consequences when using features in the AdWMGUI software.
"""

def normalize(text):
    return [line.strip() for line in text.replace('\r\n', '\n').replace('\r', '\n').split('\n') if line.strip()]

def check_agreement_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return normalize(content) == normalize(adwmgui_agreement)
    except FileNotFoundError:
        return False