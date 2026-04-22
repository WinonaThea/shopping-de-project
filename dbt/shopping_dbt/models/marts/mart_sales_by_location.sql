select
    location,
    count(*) as total_transactions,
    sum(purchase_amount_usd) as total_sales,
    avg(purchase_amount_usd) as avg_sales
from {{ ref('stg_customer_shopping_trends') }}
group by 1