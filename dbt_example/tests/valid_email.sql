{% test valid_email(model, column_name) %}

WITH validation AS (
    SELECT {{ column_name }} AS email
    FROM {{ model }}
    WHERE {{ column_name }} NOT LIKE '%_@__%.__%'
)

SELECT COUNT(*)
FROM validation

{% endtest %}
