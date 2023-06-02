#!/bin/sh

# Author : Karin Nordin

awk '
BEGIN {
    idx = 1
}
$7 - $6 + 1 >= 1000 && $11 - $10 + 1 >= 1000 {
    if (!($1 in vertex_map)) {
        vertex_map[$1] = idx
        idx++
    }
    if (!($2 in vertex_map)) {
        vertex_map[$2] = idx
        idx++
    }
    print vertex_map[$1], vertex_map[$2], $6, $7, $8, $10, $11, $12
}
' data.txt > "$translated_data"
