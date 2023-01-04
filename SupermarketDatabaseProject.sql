---*/ CREATING THE grocery_store Table in the AZSUPERMARKET Database

CREATE TABLE grocery_store(
product_id INTEGER IDENTITY(1,1),
name VARCHAR(225),
price_per_pack INTEGER,
packs INTEGER,
product_category VARCHAR(50));

SELECT * FROM grocery_store 


--*/The price_per_pack Column was previously price and was renamed to "price_per_pack" because Stating as price would mean all the packs is priced at that amount.
--Example price(Apples) = 3 This might mean that the price of all the 200 apples is 3 which is incorrect. 
--So stating prce_per_pack(Apples) =3 means that the price of 1 apple pack out of the 200 packs is 3.This is more clear.

sp_rename 'grocery_store.price' , 'price_per_pack'

--*/ The packs Column was previously packs and was renamed to "packs".
--Example: The price of 1 Apple pack is 4, and there are 150 packs.

sp_rename 'grocery_store.packs' , 'packs';

--*/INSERTING data into the groery_store Table which is in the AZSUPERMARKET Database

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Apples',4,150,'Fruits');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Bananas',4 ,150,'Fruits');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Oranges',5,200,'Fruits');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Straberries',6,320,'Fruits');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Grapes',10,129,'Fruits');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Broccoli',12,100,'Vegetables');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Spinach',4,210,'Vegetables');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Tomatoes',15,400,'Vegetables');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Peppers',15,320,'Vegetables');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Onions',10,200,'Vegetables');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Chicken',30,320,'Meat');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Beef',25,410,'Meat');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Pork',20,130,'Meat');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Lamb',35,120,'Meat');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Salmon',13,230,'Fish');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Cod',20,26,'Fish');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Tilapia',32,150,'Fish');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Milk',9,270,'Dairy');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Cheese',7,100,'Dairy');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Yogurt',12,240,'Dairy');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Butter',17,60,'Dairy');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Bread',10,400,'Bread and grains');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Rice',30,330,'Bread and grains');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Pasta',32,130,'Bread and grains');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Oats',15,240,'Bread and grains');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Soup',26,170,'Canned goods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Beans',17,201,'Canned goods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('vegetables',18,204,'Canned goods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Fruit',23,160,'Canned goods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Sugar',9,390,'Baking items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Flour',13,109,'Baking items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Baking powder',28,13,'Baking items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Chips',12,280,'Snacks');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Crackers',8,105,'Snacks');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Cookies',17,207,'Snacks');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Water',6,500,'Beverages');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Soda',15,190,'Beverages');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Juice',14,26,'Beverages');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Coffee',16,19,'Beverages');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Tea',8,150,'Beverages');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Pizza',19,100,'Frozen foods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Ice cream',7,109,'Froze foods');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Toothpaste',5,100,'Personal care items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Shampoo',27,78,'Personal care items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Soap',10,201,'Personal care items');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Laundy detergent',17,74,'Cleaning supplies');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('All-purpose cleaner',20,90,'Cleaning supplies');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('dog food',40,65,'Pet supplies');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Cat food',30,85,'Pet supplies');

INSERT INTO grocery_store (name , price_per_pack ,packs, product_category)
VALUES ('Litter',16,45,'Pet supplies');









