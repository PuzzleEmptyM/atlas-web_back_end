-- Old school band
SELECT
  name AS band_name,
  (CASE
     WHEN split IS NULL THEN YEAR(CURDATE()) - formed
     ELSE split - formed
   END) AS lifespan
FROM
  metal_bands
WHERE
  main_style = 'Glam rock'
ORDER BY
  lifespan DESC;
