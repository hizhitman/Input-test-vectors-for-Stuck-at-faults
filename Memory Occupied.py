from main import main
%load_ext memory_profiler
%mprun -f  main main()
