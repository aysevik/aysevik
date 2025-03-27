import java.util.Objects;

public class BattleShip {
    public static void main(String[] args) {
        boolean[][] map = createMap(8, 6);
        placeShip(map, 1, 2, 3, true);
        placeShip(map, 2, 0, 2, false);
        printMap(map);
    }

    public static void placeShip(boolean[][] map, int startRow, int startColumn, int size, boolean isVertical) {
        Objects.requireNonNull(map);
        int endRow = isVertical ? startRow + size - 1 : startRow;
        int endColumn = !isVertical ? startColumn + size - 1 : startColumn;
        assertIsInMap(map, startRow, startColumn, "Start position (%02d, %02d) not in map");
        assertIsInMap(map, endRow, endColumn, "End position (%02d, %02d) not in map");

        if (isVertical) {
            for (int row = startRow; row <= endRow; row++) {
                if (isOccupied(map, row, startColumn)) {
                    throw new IllegalArgumentException("Collission: position (%02d, %02d) already occupied!".formatted(row, startColumn));
                }
                map[row][startColumn] = true;
            }
        } else {
            for (int column = startColumn; column <= endColumn; column++) {
                if (isOccupied(map, startRow, column)) {
                    throw new IllegalArgumentException("Collission: position (%02d, %02d) already occupied!".formatted(startRow, column));
                }
                map[startRow][column] = true;
            }
        }
    }

    public static boolean isOccupied(boolean[][] map, int row, int column) {
        assertValidity(map, row, column);
        return map[row][column];
    }

    public static boolean isInMap(boolean[][] map, int row, int column) {
        Objects.requireNonNull(map);
        return row >= 0 && row < map.length && column >= 0 && column < map[row].length;
    }

    public static void assertIsInMap(boolean[][] map, int row, int column, String template) {
        if (!isInMap(map, row, column)) {
            throw new IllegalArgumentException(template.formatted(row, column));
        }
    }

    public static void assertValidity(boolean[][] map, int row, int column) {
        if (map == null) throw new IllegalArgumentException("map must be non-null");
        assertIsInMap(map, row, column, "Invalid position: (%02d, %02d)");
    }

    public static boolean[][] createMap(int rows, int columns) {
        if (rows <= 0) throw new IllegalArgumentException("Number of rows must be >= 1");
        if (columns <= 0) throw new IllegalArgumentException("Number of columns must be >= 1");
        return new boolean[rows][columns];
    }

    public static void printMap(boolean[][] map) {
        for (boolean[] row : map) {
            for (boolean cell : row) {
                System.out.printf("%s ", cell ? "*" : ".");
            }
            System.out.println();
        }
    }
}
