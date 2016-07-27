# Transform
The Transform plugin provides access to the Level 3 representations of a file's data.  All of the features offered by this plugin are derived by implementing \verb/radare/--a tool for disassembling and debugging binary files\cite{radare}
\begin{itemize}
\item Disassembly: The disassembly of a file is acquired by running the \verb/get_disassembly/ function, which uses \verb/r2pipe/, a tool for scripting \verb/radare/.  It returns the full disassembly: opcodes, memory addresses, assembly instructions, and notes.

\item Mnemonics: The \verb/get_mnemonics/ function returns a list of mnemonics that are present in a binary's instructions.

\item Functions: The \verb/get_functions/ function returns a list of the functions that are in the binary by parsing the disassembly from \verb/radare/ to return only the assembly instructions.

\item Data References: The \verb/get_data_references/ function looks for \verb/lea/ and \verb/mov/ in the assembly instructions and creates a list of the memory addresses accessed by those instructions.

\item Jump Targets: the \verb/get_jump_targets/ function looks through the disassembly of a binary and filters out any line that doesn't contain a jump command, leaving a list of the jump instructions.\newline
\end{itemize}
