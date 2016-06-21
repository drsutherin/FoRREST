using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace euler {
    class Problem15 {

        public static void Main(string[] args) {
            new Problem15().Dynamic();
            new Problem15().Combinatorics();
        }

        public void Dynamic() {
            Stopwatch clock = Stopwatch.StartNew();

            const int gridSize = 20;
            
            long[,] grid = new long[gridSize+1, gridSize+1];

            for (int i = 0; i < gridSize; i++) {
                grid[i, gridSize] = 1;
                grid[gridSize,i] = 1;
            }

            for (int i = gridSize - 1; i >= 0; i--) {
                for (int j = gridSize - 1; j >= 0; j--) {
                    grid[i, j] = grid[i+1, j] + grid[i, j+1];
                }
            }
                       
            clock.Stop();
            Console.WriteLine("In a {0}x{0} grid there are {1} possible paths.", gridSize, grid[0,0]);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

       
        public void Combinatorics() {
            Stopwatch clock = Stopwatch.StartNew();

            const int gridSize = 20;

            long paths = 1;

            for (int i = 0; i < gridSize; i++) {
                paths *= (2 * gridSize) - i;
                paths /= i + 1;
            }


            clock.Stop();
            Console.WriteLine("In a {0}x{0} grid there are {1} possible paths.", gridSize, paths);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

     


    }
}

