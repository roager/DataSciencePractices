/*  Bootcamp Data Science - Ejercicio semana 15 - Gerardo Rodríguez */  

/*  Creación de Tablas */  
CREATE TABLE Clientes (
cliente_id INT PRIMARY KEY,
nombre VARCHAR(50),
email  VARCHAR(50),
fecha_registro DATE 
);
CREATE TABLE Productos (
producto_id INT PRIMARY KEY,
nombre VARCHAR(50),
categoria  VARCHAR(50),
precio FLOAT 
);
CREATE TABLE Transacciones (
transaccion_id INT PRIMARY KEY,
cliente_id INT,
producto_id INT,
cantidad INT,
fecha DATE 
);
/*  Carga de datos */  
INSERT INTO Clientes (cliente_id,nombre,email,fecha_registro) VALUES
(1, 'Ana Madrid', 'Ana@Madrid.com', '2024-05-23'),
(2, 'Luis Barcelona', 'Luis@Barcelona.com', '2024-05-30'),
(3, 'Marta Sevilla', 'Marta@Sevilla.com', '2024-05-28');
INSERT INTO Productos (producto_id,nombre,categoria,precio) VALUES
(1, 'VS CODE', 'Código', '200.00'),
(2, 'MARIADB', 'Almacenamiento', '300.00'),
(3, 'POWERBI', 'Visualización', '400'),
(4, 'Python', 'Análisis', '500.00');
INSERT INTO Transacciones (transaccion_id,cliente_id,producto_id,cantidad,fecha) VALUES
(1, 1, 4, 2, '2024-05-23'),
(2, 2, 3, 3, '2024-05-30'),
(3, 3, 2, 4, '2024-05-28'),
(4, 1, 3, 2, '2024-05-23'),
(5, 1, 2, 2, '2024-05-23');
/*  Consulta número de transacciones por cliente ordenada desc por el total de transacciones */  
SELECT
  t.cliente_id, c.nombre,
  COUNT(transaccion_id) AS Cantidad_Total_Transacciones
FROM Transacciones t
LEFT JOIN Clientes c
ON t.cliente_id=c.cliente_id
GROUP BY t.cliente_id
ORDER BY Cantidad_Total_Transacciones DESC;
/*  Consulta gasto total de transacciones por cliente ordenada desc por el gasto total  */
SELECT
  t.cliente_id, 
  SUM(p.precio * t.cantidad) AS gasto_total_cliente
FROM Transacciones t
LEFT JOIN Productos p
ON t.producto_id=p.producto_id
GROUP BY t.cliente_id
ORDER BY gasto_total_cliente DESC;
/*  Consulta el producto más vendido  */
SELECT
  t.producto_id, p.nombre,
  SUM(p.precio * t.cantidad) AS gasto_total_producto
FROM Transacciones t
LEFT JOIN Productos p
ON t.producto_id=p.producto_id
GROUP BY t.producto_id
ORDER BY gasto_total_producto DESC;
/*  Consulta el día con mayor monto vendido  */
SELECT
  t.fecha,
  SUM(p.precio * t.cantidad) AS gasto_total_fecha
FROM Transacciones t
LEFT JOIN Productos p
ON t.producto_id=p.producto_id
GROUP BY t.fecha
ORDER BY gasto_total_fecha DESC;