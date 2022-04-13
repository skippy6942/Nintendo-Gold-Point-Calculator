"""
Nintendo Gold Point Calculator
By skippy_69
Simple Python Program 

 /$$   /$$/$$           /$$                            /$$                 /$$$$$$          /$$      /$$       /$$$$$$$         /$$           /$$            /$$$$$$          /$$                  /$$           /$$                      
| $$$ | $|__/          | $$                           | $$                /$$__  $$        | $$     | $$      | $$__  $$       |__/          | $$           /$$__  $$        | $$                 | $$          | $$                      
| $$$$| $$/$$/$$$$$$$ /$$$$$$   /$$$$$$ /$$$$$$$  /$$$$$$$ /$$$$$$       | $$  \__/ /$$$$$$| $$ /$$$$$$$      | $$  \ $$/$$$$$$ /$$/$$$$$$$ /$$$$$$        | $$  \__/ /$$$$$$| $$ /$$$$$$$/$$   /$| $$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$ 
| $$ $$ $| $| $$__  $|_  $$_/  /$$__  $| $$__  $$/$$__  $$/$$__  $$      | $$ /$$$$/$$__  $| $$/$$__  $$      | $$$$$$$/$$__  $| $| $$__  $|_  $$_/        | $$      |____  $| $$/$$_____| $$  | $| $$|____  $|_  $$_/  /$$__  $$/$$__  $$
| $$  $$$| $| $$  \ $$ | $$   | $$$$$$$| $$  \ $| $$  | $| $$  \ $$      | $$|_  $| $$  \ $| $| $$  | $$      | $$____| $$  \ $| $| $$  \ $$ | $$          | $$       /$$$$$$| $| $$     | $$  | $| $$ /$$$$$$$ | $$   | $$  \ $| $$  \__/
| $$\  $$| $| $$  | $$ | $$ /$| $$_____| $$  | $| $$  | $| $$  | $$      | $$  \ $| $$  | $| $| $$  | $$      | $$    | $$  | $| $| $$  | $$ | $$ /$$      | $$    $$/$$__  $| $| $$     | $$  | $| $$/$$__  $$ | $$ /$| $$  | $| $$      
| $$ \  $| $| $$  | $$ |  $$$$|  $$$$$$| $$  | $|  $$$$$$|  $$$$$$/      |  $$$$$$|  $$$$$$| $|  $$$$$$$      | $$    |  $$$$$$| $| $$  | $$ |  $$$$/      |  $$$$$$|  $$$$$$| $|  $$$$$$|  $$$$$$| $|  $$$$$$$ |  $$$$|  $$$$$$| $$      
|__/  \__|__|__/  |__/  \___/  \_______|__/  |__/\_______/\______/        \______/ \______/|__/\_______/      |__/     \______/|__|__/  |__/  \___/         \______/ \_______|__/\_______/\______/|__/\_______/  \___/  \______/|__/      
"""
# imports

import time
import webbrowser

# title screen with language selection

print("Nintendo Gold Point Calculator / 任天度ゴルドーポイントのカルキュレーター / Calculatrice Nintendo Goldpoint / Calcolatrice Goldpoint Nintendo\n")
time.sleep(0.3)
while(True):
    print("Select Language / 言語を選択する / choisissez la langue / seleziona la lingua\n")
    print("English (UK) - [en-GB]\nEnglish (US) - [en-US]\n日本語 - [jp]\nFrançais - [fr]\nItaliano - [it]")
    lang = input("(Enter Language Code / 言語コードを入力してください / entrez le code de langue / inserite il codice della lingua)\n(or type \"info\" for more information on star points / スターポイントの詳細については、「info」と入力してください / ou entrez \"info\" pour plus d'informations sur les Star Points / oppure inserisci \"info\" per maggiori informazioni sui Star Points\n")
    
# when user enters "info" opens browser and navigates to the my nintendo gold point website

    if lang == "info":
        print("Directing to browser... / ブラウザに転送しています... / Direction vers le navigateur... / Indirizzamento al browser...")
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        webbrowser.open("https://my.nintendo.com/about_gold_point")
        continue

    elif lang == "en-GB":
        
        #en-GB
        while(True):
         # asks user option
            print("Please select an option")
            time.sleep(0.1)
            print("1: Calculate Currency to Star Point")
            time.sleep(0.1)
            print("2: Calculate Gold Point to Currency")
            time.sleep(0.1)
            userSelection = int(input("Enter Option: "))

            if userSelection == 1:
                opt1CurrencyInput = float(input("Enter Amount (£): "))
                opt1CurrencyInput = ((opt1CurrencyInput*100)/100)*5
                opt1CurrencyInput = round(opt1CurrencyInput)
                print("Goldpoint = " + str(opt1CurrencyInput))
                endProg = input("End programme? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            elif userSelection == 2:
                opt2CurrencyInput = float(input("Enter Amount (★): "))
                opt2CurrencyInput = ((opt2CurrencyInput/5)*100)/100
                opt2CurrencyInput = round(opt2CurrencyInput, 2)
                print("Amount to spend = £" + str(opt2CurrencyInput))
                endProg = input("End programme? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            else:
             # repeats to beginning of while loop
                print("Please enter a valid selection")
                continue

    elif lang == "en-US":
        
        #en-US
        while(True):
            print("Please select an option")
            time.sleep(0.1)
            print("1: Calculate Currency to Gold Point")
            time.sleep(0.1)
            print("2: Calculate Gold Point to Currency")
            time.sleep(0.1)
            userSelection = int(input("Enter Option: "))

            if userSelection == 1:
                opt1CurrencyInput = float(input("Enter Amount ($): "))
                opt1CurrencyInput = ((opt1CurrencyInput*100)/100)*5
                opt1CurrencyInput = round(opt1CurrencyInput)
                print("Goldpoint = " + str(opt1CurrencyInput))
                endProg = input("End program? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            elif userSelection == 2:
                opt2CurrencyInput = float(input("Enter Amount (★): "))
                opt2CurrencyInput = ((opt2CurrencyInput/5)*100)/100
                opt2CurrencyInput = round(opt2CurrencyInput, 2)
                print("Amount to spend = $" + str(opt2CurrencyInput))
                endProg = input("End program? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            else:
                print("Please enter a valid selection")
                continue
        
    elif lang == "jp":
        
        #en-US
        while(True):
            print("オプションを選択してください")
            time.sleep(0.1)
            print("1: 円にゴルドーポイントを計算する")
            time.sleep(0.1)
            print("2: ゴルドーポイントに円を計算する")
            time.sleep(0.1)
            userSelection = int(input("オプションを入力: "))

            if userSelection == 1:
                opt1CurrencyInput = float(input("金額を入力 (¥): "))
                opt1CurrencyInput = (opt1CurrencyInput/100)*5
                opt1CurrencyInput = round(opt1CurrencyInput)
                print("ゴルドーポイント = " + str(opt1CurrencyInput))
                endProg = input("プログラムを終了？ (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            elif userSelection == 2:
                opt2CurrencyInput = float(input("金額を入力 (★): "))
                opt2CurrencyInput = ((opt2CurrencyInput/5)*100)
                opt2CurrencyInput = round(opt2CurrencyInput, 2)
                print("使う金額 = ¥" + str(opt2CurrencyInput))
                endProg = input("プログラムを終了？ (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            else:
                print("有効なオプションを入力してください")
                continue
    
    elif lang == "fr":
        
        #fr
        while(True):
            print("veuillez sélectionner une option")
            time.sleep(0.1)
            print("1: Calculer de la devise au Gold Point")
            time.sleep(0.1)
            print("2: Calculer du Gold Point à la devise")
            time.sleep(0.1)
            userSelection = int(input("saisissez l'option: "))

            if userSelection == 1:
                opt1CurrencyInput = float(input("entrer le montant (€): "))
                opt1CurrencyInput = ((opt1CurrencyInput*100)/100)*5
                opt1CurrencyInput = round(opt1CurrencyInput)
                print("Goldpoint = " + str(opt1CurrencyInput))
                endProg = input("terminer le programme? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            elif userSelection == 2:
                opt2CurrencyInput = float(input("entrer le montant (★): "))
                opt2CurrencyInput = ((opt2CurrencyInput/5)*100)/100
                opt2CurrencyInput = round(opt2CurrencyInput, 2)
                print("montant à dépenser = €" + str(opt2CurrencyInput))
                endProg = input("terminer le programme? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            else:
                print("veuillez entrer une option valide")
                continue
    
    elif lang == "it":
        
        #it
        while(True):
            print("Per favore selezionate un'opzione\n")
            time.sleep(0.1)
            print("1: Calcolare la valuta a Gold Point\n")
            time.sleep(0.1)
            print("2: Calcolare Gold Point a la valuta\n")
            time.sleep(0.1)
            userSelection = int(input("inserite un'opzione: "))

            if userSelection == 1:
                opt1CurrencyInput = float(input("inserite un valore (€): "))
                opt1CurrencyInput = ((opt1CurrencyInput*100)/100)*5
                opt1CurrencyInput = round(opt1CurrencyInput)
                print("Goldpoint = " + str(opt1CurrencyInput) + "\n")
                endProg = input("terminare il programma? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            elif userSelection == 2:
                opt2CurrencyInput = float(input("inserite un valore (★): "))
                opt2CurrencyInput = ((opt2CurrencyInput/5)*100)/100
                opt2CurrencyInput = round(opt2CurrencyInput, 2)
                print("valore da spendere = €" + str(opt2CurrencyInput))
                endProg = input("terminare il programma? (Y/N): ")
                if endProg == "Y" or endProg == "y":
                    exit()
                elif endProg == "N" or endProg == "n":
                    break

            else:
                print("si prega di inserire una selezione valida")
                continue
