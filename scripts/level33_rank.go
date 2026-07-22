package main

import (
    "encoding/binary"
    "fmt"
    "io"
    "os"
)

const p byte = 7

func rank(rows [][]byte, n int) int {
    pivot := 0
    inv := [7]byte{0, 1, 4, 5, 2, 3, 6}
    for col := 0; col < n && pivot < len(rows); col++ {
        sel := -1
        for r := pivot; r < len(rows); r++ {
            if rows[r][col] != 0 {
                sel = r
                break
            }
        }
        if sel < 0 {
            continue
        }
        rows[pivot], rows[sel] = rows[sel], rows[pivot]
        scale := inv[rows[pivot][col]]
        if scale != 1 {
            row := rows[pivot]
            for c := col; c < n; c++ {
                row[c] = byte((uint16(row[c]) * uint16(scale)) % 7)
            }
        }
        prow := rows[pivot]
        for r := pivot + 1; r < len(rows); r++ {
            factor := rows[r][col]
            if factor == 0 {
                continue
            }
            row := rows[r]
            for c := col; c < n; c++ {
                v := int(row[c]) - int(factor)*int(prow[c])
                v %= 7
                if v < 0 {
                    v += 7
                }
                row[c] = byte(v)
            }
        }
        pivot++
        if pivot%100 == 0 || pivot == n {
            fmt.Printf("pivot=%d/%d\n", pivot, n)
        }
    }
    return pivot
}

func cloneBlocks(blocks []byte, n, count int) [][]byte {
    rows := make([][]byte, count*n)
    stride := n * n
    for b := 0; b < count; b++ {
        base := b * stride
        for r := 0; r < n; r++ {
            row := make([]byte, n)
            copy(row, blocks[base+r*n:base+(r+1)*n])
            rows[b*n+r] = row
        }
    }
    return rows
}

func main() {
    if len(os.Args) != 2 {
        fmt.Fprintln(os.Stderr, "usage: level33_rank dense.bin")
        os.Exit(2)
    }
    f, err := os.Open(os.Args[1])
    if err != nil { panic(err) }
    defer f.Close()
    var n32, blocks32 uint32
    if err := binary.Read(f, binary.LittleEndian, &n32); err != nil { panic(err) }
    if err := binary.Read(f, binary.LittleEndian, &blocks32); err != nil { panic(err) }
    n, blockCount := int(n32), int(blocks32)
    if blockCount != 4 { panic("expected four operator blocks") }
    data := make([]byte, blockCount*n*n)
    if _, err := io.ReadFull(f, data); err != nil { panic(err) }

    fmt.Printf("n=%d blocks=%d\n", n, blockCount)
    r11 := rank(cloneBlocks(data, n, 2), n)
    fmt.Printf("rank11=%d dim11=%d\n", r11, n-r11)
    r1119 := rank(cloneBlocks(data, n, 4), n)
    fmt.Printf("rank1119=%d dim1119=%d eliminated=%v\n", r1119, n-r1119, r1119 == n)
    if r1119 != n { os.Exit(3) }
}