# Курсовая работа по теме "Исследование нейросетевых методов построения кликовой модели для задач информационного поиска"

* Обработка датасета: `/src/scripts/`
* Модификация GraphCM: [github.com/VictorDotZ/GraphCM](https://github.com/VictorDotZ/GraphCM)
* session_ids тренировочной части для идентичности (первая `./data` из форка GraphCM после обработки скриптами):

```bash
./data/VK/train_per_query_quid.txt | awk -F"\t" '{ print $1 }' > ./../PyClick/examples/data/VK_train_sid.txt
```

> Для тестовой аналогично с заменой train на test соответственно

* Логи и веса: [click-models-logs.tar.gz]([https:google.com](https://cloud.mail.ru/public/Jt7i/J2UTuL8i1))
