dir_dict = {
    '0': (0, 0.5),
    '1': (0, -0.5),
    '2': (-0.5, 0),
    '3': (0.5, 0)
}
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    atoms = [list(map(int, input().split())) for _ in range(n)]
    # x, y, dir, k(eng)
    ans = 0

    atoms_dict = {}
    for atom in atoms:
        atoms_dict[(atom[0], atom[1])] = [float(atom[0]), float(atom[1]), atom[2], atom[3]]
    # print(atoms_dict)
    while atoms_dict:
        temp_dict = {}
        for chk in atoms_dict.values():  # chk : 0 : x  /  1 : y  /  2 : dir  /  3 : [k]
            moved_x, moved_y = chk[0] + dir_dict[str(chk[2])][0], chk[1] + dir_dict[str(chk[2])][1]
            if moved_x > 1000 or moved_x < -1000 or moved_y > 1000 or moved_y < -1000:continue

            key = (moved_x, moved_y)


            if key in temp_dict:
                temp_dict[key].append(chk[3])
            else:
                temp_dict[key] = [moved_x, moved_y, chk[2], chk[3]]

        atoms_dict = {}
        for k, v in temp_dict.items():
            if len(v) > 4:
                ans += sum(v[3:])
            else:
                atoms_dict[k] = v


    print(f'#{tc} {ans}')
    # break
