# Pranav Purwar's CV

- Email: [purwarpranav80@gmail.com](mailto:purwarpranav80@gmail.com)
- Location: Delhi, India
- GitHub: [PranavPurwar](https://github.com/PranavPurwar)
- LinkedIn: [pranavpurwar](https://linkedin.com/in/pranavpurwar)


# Summary
Systems Engineer working on **JVM internals**, **compilers**, **AI infrastructure**, and **Android OS virtualization**. Creator of **Cosmic IDE** (**700+ stars**, **100+ forks**), bringing rootless Arch Linux environments to Android, and **Bryte AI Platform** (GraphRAG & FSRS v4 scheduling). Contributor to Android developer tools with **1.2M+ downloads** and **100k+ MAU**.

# Experience
## **Cosmic IDE | Creator & Architect**

[**GitHub**](https://github.com/aload0/Cosmic-IDE)

Aug 2021 – present

- **Rootless Linux Environment**: Built a full Arch Linux ARM runtime on Android without root or proot using a custom `glibc` runtime and `LD_PRELOAD` shims to intercept `execve`/`execvp`/`posix_spawn`, DNS, and filesystem syscalls.

- **Recursive Process Sandboxing**: Intercepted process creation chains ensuring child processes (e.g. Gradle daemons, Cargo workers) automatically inherit the shim environment and sandbox boundaries.

- **Terminal & Package Management**: Built an integrated PTY terminal emulator with process group signal handling (`SIGINT`/Ctrl+C propagation) and native Arch Linux `pacman` package manager support.

- **Language & Project Toolchains**: Built a plugin marketplace delivering complete language, project build system (Gradle, Cargo, Maven), and on-device Language Server Protocol (LSP) support across **11+ languages** (Rust, Java, Kotlin, Scala, Go, C/C++, Python, etc.).

- **Plugin Architecture**: Engineered dynamic plugin loading for language definitions, custom build commands, and syntax schemas decoupled from core app releases.



## **Bryte AI Platform (Open-Source) | Creator & Lead Developer**

[**GitHub**](https://github.com/Bryte-Edu/server)

Sept 2024 – present

- Built a **Kotlin Multiplatform** backend (Ktor CIO) ingesting PDFs (Mistral OCR), YouTube transcripts (NewPipe extractor), and web pages into structured notes.

- Implemented **GraphRAG** in Neo4j with **1024-dim vector indexing**, weighted Cypher queries balancing document vs cross-document links, automatic semantic chunk interlinking, and Cohere reranking.

- Wrote a native Kotlin port of **FSRS v4** (spaced repetition algorithm) to compute card stability, difficulty, and retrievability without external dependencies.

- Orchestrated multi-step LLM workflows using JetBrains Koog with context compression, plus a streaming Markdown parser with mid-stream table recovery.

- Streamed generated flashcards and questions in real time using type-safe **`kotlinx.rpc` over WebSockets**, multiplexing multiple services over a single connection.



## **OpenJDK & Kotlin Compiler Ports (Android)**

[**OpenJDK**](https://github.com/PranavPurwar/javac-android) | [**Kotlin**](https://github.com/PranavPurwar/kotlinc-android)

Sept 2023 – present

- **Compiler Ports**: Ported `javac` (OpenJDK 27 EA, Java 26 support) and `kotlinc` (Kotlin 2.4/2.5) to run directly on Android Runtime (**ART**); published artifacts to JitPack.

- **NIO & Memory Fixes**: Bypassed Android's restricted NIO via custom `ZipFileSystem` for `ct.sym`; used HiddenApi Bypass to invoke `NioUtils.freeDirectBuffer`, fixing fatal off-heap OOM crashes during JAR parsing.

- **Upstream Contribution**: Authored PR [`JetBrains/kotlin#5146`](https://github.com/JetBrains/kotlin/pull/5146) fixing a direct-buffer memory leak in `ZipImplementation` when using `-Xuse-fast-jar-file-system`.



## **Sketchware-Pro | Core Team**

[**GitHub**](https://github.com/Sketchware-Pro/Sketchware-Pro)

Aug 2021 – present

- Core team member for Android IDE (**1.7k+ stars**, **670+ forks**, **100k+ MAU**) integrating ported Kotlin/Java compilers.

- Integrated **R8/D8 Code Shrinker** and added Java 9/11+ compilation pipelines, cutting output APK sizes by **~40%**.

- Engineered on-device compile-time **ViewBinding generator** from XML layouts and recursive AAR/JAR dependency resolver.



## **Reef | Creator**

[**GitHub**](https://github.com/aload0/Reef)

Sept 2024 – present

- Built an open-source Android screen time & productivity app (**320+ stars**, on IzzyOnDroid) with **Jetpack Compose** and Material 3 Expressive.

- Normalized inconsistent `UsageStatsManager` events across fragmented OEM ROMs (MIUI, OneUI) to accurately calculate per-app screen time.

- Implemented real-time app and website blocking, Pomodoro focus timers, and routines using `AccessibilityService` and `NotificationListenerService`.



# Skills
**Languages:** Kotlin, Java, Python, TypeScript, C, JVM Bytecode, DEX/ART

**Compiler & Systems:** OpenJDK, kotlinc, ART Runtime, LSP, Gradle, R8/D8, glibc, LD_PRELOAD, Linux Virtualization, ELF/PTY, HiddenApi Bypass

**Backend & AI Infrastructure:** Ktor, Neo4j, GraphRAG, Cypher, FSRS v4, LLM Agents (Koog), kotlinx.rpc, WebSockets, Mistral AI, Cohere, SSE Streaming

**Mobile & Platforms:** Android SDK, Jetpack Compose, Kotlin Multiplatform (KMP), Material 3 Expressive, IzzyOnDroid / F-Droid
