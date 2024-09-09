Select 
    c.name as Customers
From
    Customers as c Left Join Orders as o
On 
    c.id = o.customerId
Where
    o.id is Null