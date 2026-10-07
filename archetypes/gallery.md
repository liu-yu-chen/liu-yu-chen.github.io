+++
title = '{{ replace .Name "-" " " | title }}'
date = '{{ .Date }}'
description = ''
cover = 'images/albums/your-photo.jpg'
draft = true
[[photos]]
src = 'images/albums/your-photo.jpg'
caption = 'Describe your photo here'
+++

{{< photos >}}
