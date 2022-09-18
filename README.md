# tg2wa_bot
Асинхронный бот для конвертации стикерпаков Telegram в формат Whatsapp.

Системные требования:
-linux x64 (как вариант возможно использование macos, совместимость с windows упирается в проблемы сборки исполняемого пакета tgs_to_png для конвертации анимированных стикеров)
-python 3.*
-ffmpeg (https://ffmpeg.org/)
-tgs_to_png (основное приложение в https://github.com/ed-asriyan/tgs-to-gif)

код написан из расчета, что использование оперативной памяти будет минимизировано, тогда как HDD/SSD будут постоянно гонять массивы данных в темп директориях.

Как пользоваться:
Да все на самом деле просто, после установки зависимостей запустите бота командой python3 tg2wa.py
При первом запуске необходимо ввести в терминале ваши api_id и api_hash (получить можно по ссылке https://my.telegram.org/apps) и bot_token (как и всегда, получить можно у https://t.me/BotFather)
После успешного запуска бота в корневом каталоге добавится файл с токеном бота и sqlite3 база сессии pyrogram.
Почему используется именно pyrogram? - хочется заранее исключить проблемы с передачей больших файлов (MTProto вместо Bot API)

Использовать настроенный бот просто:
-Установите на своф смартфон приложение Sticker Maker.
	Версия для Google Play (Android) https://play.google.com/store/apps/details?id=com.marsvard.stickermakerforwhatsapp
	Версия для App store (iOS) https://apps.apple.com/us/app/sticker-maker-studio/id1443326857
-Отправьте стикер или ссылку на стикерпак боту
-Дождитесь выполнения конвертации
-После успешного завершения работы скрипта бот вернет архив со стикерами, совместимыми с Whatsapp. Если в стикерпаке больше 30 стикеров бот вернет несколько архивов
-Откройте полученный файл в приложении Sticker Maker
-Нажмите «Добавить в библиотеку», а затем «Добавить в WhatsApp». Подтвердите действие.
-Все готово, можно делиться стикерами в своих группах.

Бота запустил для ознакомления здесь http://t.me/tg_to_wa_bot, но не могу гарантировать что он будет работать постоянно.
