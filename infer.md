# Infer


get_cfg/, which uses \verb/angr/ and an extension of it called \verb/angr-utils/\cite{angr-utils}.  The CFG is saved as a PNG image file located in the same directory as the file upon which it was called, and it is displayed immediately.  An example of a CFG output by FoRREST is given at the bottom of this page in Figure 6.

\item System Calls: Not currently implemented, considering using GNU library's \verb/strace/

\item Function Traces: Not currently implemented, considering calling FoRREST's \verb/get_functions/ along with the disassembly to determine where functions are called, and by what other functions.

\begin{figure}[h]
\centering
\fbox{\includegraphics[width=0.45\textwidth]{crackme0x00a_cfg}}
\cprotect\caption{An example of a CFG generate by calling FoRREST's \verb/get_cfg/ function on \verb/crackme0x00a/ from RPI's Modern Binary Exploitation course\cite{modernbinaryexploitation2015}.}
\end{figure}

\item Code Slices: Not currently implemented, planning to use \verb/angr/ to perform back-slicing.

\item Intermediate Representation: Currently being developed using \verb/angr/ and its dependency \verb/PyVex/\cite{shoshitaishvili2015firmalice}.

\item Decompilation: The decompilation of a file can be created by calling \verb/decompile/, which uses \verb/boomerang/ to translate the binary into C code.  The file is saved in the \verb/outputs/ directory, within FoRREST's root directory. 

\item Stack Frames: Not currently implemented.

\item Symbolic Execution: Not currently implemented, planning to use \verb/angr/'s execution engine.

\item Deobfuscation:  Currently being developed, we are planning to use a tool called \verb/metasm/.

\item Taint Analysis: Not currently implemented, considering using a combination of FoRREST's \verb/get_data_references/ and \verb/slice/ functions.