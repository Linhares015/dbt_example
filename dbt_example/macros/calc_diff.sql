{% macro calc_diff(data_inicial, data_final) %}
    DATEDIFF(DAY, {{ data_inicial }}, {{ data_final }})
{% endmacro %}
