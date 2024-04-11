#!/bin/bash
while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ "$line" == "ALEMBIC_INIT="* ]]; then
        ALEMBIC_INIT="${line#*=}"
        break
    fi
done < .env

if [ "$ALEMBIC_INIT" != "true" ]; then
    if alembic upgrade head; then
        sed -i 's/ALEMBIC_INIT=.*/ALEMBIC_INIT=true/' .env
        echo "Парсим данные из реестра фильмов, примерно 25-30 минут (более 100 000 записей). Пользоваться API уже можно (данные будут обновляться). Пожалуйста, не завершайте программу вручную, пока не увидите оповещения о завершении парсинга."
        python main.py
        echo "Внимание! Все данные выгружены и доступны для отображения."
    else
        exit 1
    fi
fi