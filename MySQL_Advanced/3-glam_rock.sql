-- Old school band
SELECT DISTINCT
  band_name,
  (IFNULL(split, 2020)-formed) AS lifespan
FROM
  metal_bands
WHERE
  main_style = 'Glam rock'
ORDER BY
  lifespan DESC;
