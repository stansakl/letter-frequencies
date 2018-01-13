using System;

namespace LetterFrequencies
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            if(args.Length == 1)
            {
                Usage();
            }
        }

        static void CountLetters(string filename)
        {

        }

        static void Usage()
        {
            Console.WriteLine("Usage:");
            Console.WriteLine("\tLetterFrequencies <file name>");
        }
    }
}
