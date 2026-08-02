# Pranav Purwar's CV

- Email: [purwarpranav80@gmail.com](mailto:purwarpranav80@gmail.com)
- Location: Delhi, India
- GitHub: [PranavPurwar](https://github.com/PranavPurwar)
- LinkedIn: [pranavpurwar](https://linkedin.com/in/pranavpurwar)

# Summary

**Systems Engineer** specializing in _JVM internals_, _compiler toolchains_, _AI infrastructure_, and _Android OS-level virtualization_. Creator of **Cosmic IDE** (**686+ stars**, **100+ forks**) featuring custom glibc runtime with recursive process wrapping, and **Bryte AI Platform** with _native FSRS v4 implementation_ and _GraphRAG retrieval_. Core contributor to open-source platforms with **1.2M+ downloads** and **30k+ daily users**.

# Experience

## **Bryte AI Platform (Open-Source) | Creator & Lead Developer**

[**GitHub**](https://github.com/Bryte-Edu/server)

Sept 2024 – present

2 years

- Designed **Kotlin Multiplatform** backend infrastructure for multi-modal document ingestion (PDF/OCR via Mistral SDK, YouTube via open-source extractor, web scraping with recursive HTML cleaning and LLM-powered hierarchical reconstruction).

- Implemented production-grade **GraphRAG** with Neo4j: **1024-dim vector index** with cosine similarity, weighted Cypher queries (configurable docBias/crossDocPenalty), automatic chunk interlinking with semantic thresholds (**≥0.65**), and real-time graph visualization endpoints.

- Engineered native Kotlin port of **FSRS v4** (spaced-repetition algorithm) with exact mathematical fidelity to upstream.

- Architected stateful AI agent orchestration using JetBrains Koog framework with autonomous history compression for **100k+ token context windows**, plus resilient MarkdownStreamingParser for real-time fragmented token processing with heuristic recovery for broken table structures.

- Built full-duplex WebSocket communication via kotlinx.rpc: multiplexed SessionService and FlashcardService over single connections with type-safe contracts, enabling **real-time streaming** of generated content to clients the millisecond they are parsed.

## **Cosmic IDE | Creator & Architect**

[**GitHub**](https://github.com/Cosmic-IDE/Cosmic-IDE)

Aug 2021 – present

5 years 1 month

- Architected full Linux OS environment on Android without root, proot, or containers using custom glibc runtime with **LD_PRELOAD shims** that intercept filesystem, DNS, and process execution calls.

- Designed **recursive process sandboxing**: execve/execvp/posix_spawn interception ensures all child processes inherit shim chain, preventing any process from escaping the sandbox.

- Engineered **native PTY implementation** with proper terminal emulation, foreground process group signal handling, and Ctrl+C propagation for interactive shells.

- Built plugin-based IDE architecture with **11 language plugins** (Rust, Java, Kotlin, Scala, Gradle, Maven, Go, Gleam, C/C++, Python, Lua) using dynamic loading and marketplace system.

- Implemented complete Arch Linux ARM runtime with **pacman integration**, fake root support, and automated glibc environment generation.

- Developed full-featured IDE with **real-time code analysis**, quick fixes, and LSP support across all plugins directly on mobile.

## **OpenJDK & Kotlin Compiler Ports (Android)**

[**OpenJDK**](https://github.com/PranavPurwar/javac-android) | [**Kotlin Compiler**](https://github.com/PranavPurwar/kotlinc-android)

Sept 2023 – present

3 years

- Ported javac (**OpenJDK 27 EA**) and kotlinc (**2.4+**) to Android Runtime (**ART)**, maintaining patches synced with upstream releases.

- Rewrote javac's internal platform resolution to bypass Android's restricted NIO by implementing **custom ZipFileSystem** for ct.sym, and patched classloading incompatibilities.

- Engineered memory reclamation layer using HiddenApiBypass to invoke Android's internal NioUtils.freeDirectBuffer, preventing **fatal OOM crashes** during memory-mapped JAR parsing.

## **Official Kotlin Compiler Contribution (JetBrains/kotlin #5146)**

[**Pull Request**](https://github.com/JetBrains/kotlin/pull/5146)

Nov 2023

- Contributed to the official Kotlin compiler by resolving a **critical memory leak**, improving performance for fast JAR file system operations.

## **Sketchware-Pro | Core Team**

[**GitHub**](https://github.com/Sketchware-Pro/Sketchware-Pro)

Aug 2021 – present

5 years 1 month

- Part of core team for the IDE (**1.6k+ stars**, **100k+ MAU**, **58+ contributors**) powered by the **ported Kotlin compiler**.

- Built build-system pipeline supporting Java 9/11 compilation; integrated **R8 Code Shrinker** reducing output **APK sizes by ~40%**.

## **Reef (Digital Wellbeing & Productivity)**

[**Reef**](https://github.com/aload0/Reef)

Sept 2024 – present

2 years

- Architected system-level digital wellbeing suite navigating strict Android background execution limits and battery optimization constraints to maintain reliable per-app tracking.

- Solved severe Android **OEM fragmentation** by engineering centralized UsageCalculator normalizing telemetry across diverse manufacturer implementations (MIUI, OneUI, etc.).

- Implemented context-aware notification routing via Accessibility/Notification Listener services with complex time-boundary tracking for overnight routines.

# Skills

**Languages:** Kotlin, Java, Python, TypeScript, C, JVM Bytecode, DEX/ART

**Compiler & Toolchain:** OpenJDK, Kotlin, ART, LSP, Gradle, R8/D8, Hidden API Bypass, ELF/PTY

**Backend & AI Infrastructure:** Ktor, Neo4j (GraphRAG/Cypher), GraphRAG, FSRS v4, LLM Agents\*\*, Koog Framework, Mistral/Cohere/Gemini APIs, SSE Streaming

**Mobile & Platforms:** Android SDK, Jetpack Compose, Kotlin Multiplatform (KMP), Material You, F-Droid

**Systems Programming:** glibc, Dynamic Linking, LD_PRELOAD, Process Virtualization, Custom Linkers, Recursive Sandboxing
