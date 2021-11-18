# Новое русское вино
Сайт магазина авторского вина "Новое русское вино".
 
 ## Как установить
 Необходимо, чтобы Python3 был уже установлен затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
``` python
pip install -r requirements.txt
 ```
 
## Как пользоваться
В коде используется библиотека ```pandas``` для работы с ```Excel``` файлами. В качестве примера в файлах репозитория лежит файл ```wine.xlsx``` в котором указаны все необходимые данные для добавления нового продукта на сайт.

![](https://user-images.githubusercontent.com/83189636/142253885-96694451-0dee-4106-b816-1c0c321e0a13.PNG)
Пример заполнения ```Excel``` файла.


Откройте командную строку, перейдите к расположению файла и пропишите команду 
```python
python main.py
```
В таком случае вся продукция на сайте будет из дефолтного ```Excel``` файла, если же вы хотите использовать свою, то в таком случае пропишите:
```python
python main.py --path (путь к Excel файлу)
```
Учтите, что в вашем ```Excel``` файле необходимо использовать те же названия, что и в дефолтном (включая название листа).

После чего зайдите в браузер и пропишите в адресную строку [http://127.0.0.1:8000]().

## Пример запуска скрипта 
![Пример запуска с консоли](https://user-images.githubusercontent.com/83189636/141719041-ac52978b-6965-4e17-8fd7-11763b1c80f5.PNG)

Пример запуска скрипта с консоли

