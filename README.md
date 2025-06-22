# React Native Multi-Platform Cookiecutter Template

A comprehensive cookiecutter template for creating React Native applications that support **iOS**, **Android**, and **macOS** platforms with modern tooling, TypeScript, NativeWind (Tailwind CSS), and best practices built-in.

## 🚀 What This Template Generates

This cookiecutter template creates a fully-configured React Native project with:

- **Multi-Platform Support**: iOS, Android, and macOS applications from a single codebase
- **TypeScript**: Full TypeScript support with strict configuration and type safety
- **NativeWind**: Tailwind CSS styling system for React Native components
- **Modern Development Tools**: ESLint, Prettier, Jest, and Watchman pre-configured
- **Optimized Build System**: Metro bundler, Babel, and platform-specific build configurations
- **Automated Setup**: Post-generation hooks that install dependencies automatically
- **Testing Framework**: Jest with React Native testing utilities and example tests
- **Professional Structure**: Organized project layout with best practices

## 📋 Prerequisites

Before using this cookiecutter template, ensure you have the following installed on your system:

### System Requirements

| Tool | Version | Purpose | Installation |
|------|---------|---------|-------------|
| **Python** | 3.7+ | Required for cookiecutter | [Download Python](https://python.org/downloads/) |
| **cookiecutter** | Latest | Template engine | `pip install cookiecutter` |
| **Node.js** | 18.0+ | JavaScript runtime for React Native | [Download Node.js](https://nodejs.org/) |
| **npm** | Latest | Package manager (comes with Node.js) | Included with Node.js |
| **Git** | Latest | Version control | [Download Git](https://git-scm.com/) |

### Platform-Specific Requirements

#### For iOS and macOS Development
| Tool | Version | Required For | Installation |
|------|---------|--------------|-------------|
| **macOS** | Latest | iOS/macOS development | Required operating system |
| **Xcode** | Latest | iOS/macOS compilation | Mac App Store |
| **Xcode Command Line Tools** | Latest | Build tools | `xcode-select --install` |
| **CocoaPods** | 1.10.0+ | iOS/macOS dependency management | `sudo gem install cocoapods` |
| **iOS Simulator** | Latest | Testing on iOS | Included with Xcode |

#### For Android Development
| Tool | Version | Purpose | Installation |
|------|---------|---------|-------------|
| **Android Studio** | Latest | Android development IDE | [Download Android Studio](https://developer.android.com/studio) |
| **Android SDK** | API 31+ | Android compilation | Installed via Android Studio |
| **Java Development Kit** | 11+ | Required for Android builds | Included with Android Studio |
| **Android Emulator** | Latest | Testing on Android | Android Studio AVD Manager |

#### Development Tools
| Tool | Purpose | Installation |
|------|---------|-------------|
| **Watchman** | File watching for fast refresh | `brew install watchman` (macOS) |
| **React Native CLI** | React Native command-line tools | Installed automatically |

## 🛠 Installation

### 1. Install Cookiecutter

Choose one of the following methods to install cookiecutter:

```bash
# Using pip (recommended)
pip install cookiecutter

# Using pipx (isolated installation)
pipx install cookiecutter

# Using conda
conda install -c conda-forge cookiecutter

# Using Homebrew (macOS)
brew install cookiecutter
```

### 2. Verify Installation

```bash
# Check cookiecutter installation
cookiecutter --version

# Check other prerequisites
python --version
node --version
npm --version
git --version
```

### 3. Generate Project from Template

```bash
# Using GitHub shorthand format (recommended)
cookiecutter gh:jordyvandomselaar/react-native-macos-blank-template

# Using full GitHub URL
cookiecutter https://github.com/jordyvandomselaar/react-native-macos-blank-template

# Using local template directory
cookiecutter /path/to/react-native-macos-blank-template

# Using template with specific branch/tag
cookiecutter gh:jordyvandomselaar/react-native-macos-blank-template --checkout main
```

## 🔧 Template Customization Options

When you run cookiecutter, you'll be prompted to provide values for these variables from [`cookiecutter.json`](cookiecutter.json):

### Required Variables

| Variable | Description | Example | Validation |
|----------|-------------|---------|------------|
| **project_name** | Project directory name (filesystem-safe) | `MyReactNativeApp` | No spaces, lowercase recommended |
| **display_name** | Human-readable app name (shown in app stores) | `My React Native App` | Any characters allowed |
| **package_id** | Bundle/package identifier (reverse domain) | `com.company.myreactnativeapp` | Must follow reverse domain notation |
| **version** | Initial semantic version number | `1.0.0` | Follow semver format (x.y.z) |
| **author_name** | Your full name for package.json | `John Doe` | Used in generated package.json |
| **author_email** | Your email address | `john.doe@example.com` | Valid email format |
| **description** | Brief project description | `A new React Native multi-platform application` | Used in package.json and README |

### Advanced Variables

| Variable | Description | Default | Options |
|----------|-------------|---------|---------|
| **react_native_version** | React Native version to use | `0.78.2` | Must be valid RN version |
| **node_version** | Minimum Node.js version requirement | `>=18.0.0` | Node version specification |
| **license** | Project license type | `MIT` | `MIT`, `Apache-2.0`, `BSD-3-Clause`, `GPL-3.0`, `None` |

### Naming Conventions and Best Practices

#### project_name Guidelines
- Use PascalCase: `MyAwesomeApp`
- No spaces or special characters
- Keep it concise but descriptive
- Will be used as directory name and in various config files

#### package_id Guidelines
- Use reverse domain notation: `com.yourcompany.appname`
- All lowercase letters
- Use dots to separate components
- Must be unique in app stores
- Examples: `com.facebook.react`, `com.airbnb.maps`

#### display_name Guidelines
- User-friendly name shown in app launchers
- Can contain spaces and special characters
- Should be memorable and brandable
- Examples: `Facebook`, `Airbnb`, `My Awesome App`

## 📝 Interactive Prompt Process

### Example Session

Here's what the interactive prompt looks like:

```bash
$ cookiecutter gh:jordyvandomselaar/react-native-macos-blank-template

project_name [MyReactNativeApp]: AwesomeWeatherApp
display_name [My React Native App]: Awesome Weather
package_id [com.company.myreactnativeapp]: com.awesome.weather
version [1.0.0]: 1.0.0
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane@awesome.com
description [A new React Native multi-platform application]: A beautiful weather app for iOS, Android, and macOS
react_native_version [0.78.2]: 0.78.2
node_version [>=18.0.0]: >=18.0.0
Select license:
1 - MIT
2 - Apache-2.0  
3 - BSD-3-Clause
4 - GPL-3.0
5 - None
Choose from 1, 2, 3, 4, 5 [1]: 1

🔧 Setting up your React Native project...
============================================================
🔍 Checking requirements...
  ✅ node: v18.17.0
  ✅ npm: 9.6.7
  ✅ xcode-select: xcode-select version 2395.
  ✅ pod: 1.12.1

📦 Installing Node.js dependencies...
  ✅ npm install completed successfully

🍎 Installing iOS dependencies...
  ✅ iOS pod install completed successfully

🖥️  Installing macOS dependencies...
  ✅ macOS pod install completed successfully

📁 Created src/ directory for your application code
  ✅ Created subdirectories: components, screens, utils, types

🧹 Cleaning up template files...
  ✅ Cleanup completed

🎉 SUCCESS! Your React Native project 'Awesome Weather' has been generated!
```

## 🔄 Post-Generation Setup

After generating your project, the [`hooks/post_gen_project.py`](hooks/post_gen_project.py) script automatically performs these setup tasks:

### Automatic Setup (via hooks)

1. **Dependency Installation**
   - Runs `npm install` to install Node.js dependencies
   - Installs iOS CocoaPods with `pod install` (macOS only)
   - Installs macOS CocoaPods with `pod install` (macOS only)

2. **Project Structure Creation**
   - Creates `src/` directory for organized code structure
   - Creates subdirectories: `components/`, `screens/`, `utils/`, `types/`
   - Generates index.ts files in each subdirectory

3. **Environment Verification**
   - Checks for required tools (Node.js, npm, Xcode tools, CocoaPods)
   - Reports missing dependencies with installation instructions
   - Validates version compatibility

4. **Cleanup**
   - Removes template-specific files
   - Cleans up any build artifacts

### Manual Steps Required

#### First-Time Platform Setup

**iOS Platform:**
```bash
# Navigate to your project
cd YourProjectName

# Verify iOS setup
npx react-native doctor

# Open in Xcode (optional)
open ios/YourProjectName.xcworkspace
```

**Android Platform:**
```bash
# Open Android project in Android Studio
# File > Open > YourProjectName/android

# Verify Android setup
npx react-native doctor

# Check connected devices/emulators
adb devices
```

**macOS Platform:**
```bash
# Open in Xcode (optional)
open macos/YourProjectName.xcworkspace

# Verify macOS-specific dependencies
cd macos && pod install && cd ..
```

### First-Time Build Instructions

#### iOS First Build
```bash
# Start Metro bundler
npm start

# In a new terminal, build and run iOS
npm run ios

# Or run on specific simulator
npx react-native run-ios --simulator="iPhone 15 Pro"
```

#### Android First Build
```bash
# Ensure Android emulator is running or device connected
adb devices

# Start Metro bundler
npm start

# In a new terminal, build and run Android
npm run android
```

#### macOS First Build
```bash
# Start Metro bundler (macOS-specific)
npm run start:macos

# In a new terminal, build and run macOS
npm run macos
```

## 🚀 Development Workflow

### Starting Development

```bash
# Navigate to your project
cd YourProjectName

# Start Metro bundler (required for all platforms)
npm start
```

### Platform-Specific Commands

#### iOS Development
```bash
# Run on default iOS Simulator
npm run ios

# Run on specific iOS Simulator
npx react-native run-ios --simulator="iPhone 15 Pro"
npx react-native run-ios --simulator="iPad Pro (12.9-inch)"

# Run on physical iOS device
npx react-native run-ios --device "Your iPhone Name"

# List available iOS simulators
xcrun simctl list devices
```

#### Android Development
```bash
# Run on Android emulator/device
npm run android

# Run on specific Android device
npx react-native run-android --device-id=<device-id>

# List connected Android devices
adb devices

# Run on specific Android emulator
npx react-native run-android --avd=<avd-name>
```

#### macOS Development
```bash
# Run on macOS
npm run macos

# Alternative command
npx react-native run-macos

# Start macOS-specific Metro bundler
npm run start:macos
```

### Testing and Quality Assurance

```bash
# Run Jest tests
npm test

# Run tests in watch mode
npm run test -- --watch

# Run tests with coverage report
npm run test -- --coverage

# Run ESLint
npm run lint

# Auto-fix ESLint issues
npm run lint -- --fix

# Check TypeScript types
npx tsc --noEmit

# Run React Native environment doctor
npx react-native doctor
```

## 📁 Project Structure Overview

The generated project follows this organized structure:

```
YourProjectName/
├── 📱 MOBILE PLATFORMS
│   ├── android/                     # Android-specific code and configuration
│   │   ├── app/
│   │   │   ├── build.gradle         # Android build configuration
│   │   │   ├── proguard-rules.pro   # Code obfuscation rules
│   │   │   └── src/main/
│   │   │       ├── AndroidManifest.xml              # Android app manifest
│   │   │       ├── java/com/yourpackage/           # Java/Kotlin source code
│   │   │       │   ├── MainActivity.kt             # Main Android activity
│   │   │       │   └── MainApplication.kt          # Application entry point
│   │   │       └── res/                            # Android resources
│   │   │           ├── drawable/                   # App drawables
│   │   │           ├── mipmap-*/                   # App icons (various densities)
│   │   │           ├── values/                     # Strings, styles, colors
│   │   │           └── ...
│   │   ├── build.gradle                            # Project-level build config
│   │   ├── settings.gradle                         # Gradle project settings
│   │   ├── gradle.properties                       # Gradle configuration
│   │   └── gradle/wrapper/                         # Gradle wrapper files
│   │
│   ├── ios/                         # iOS-specific code and configuration
│   │   ├── YourProjectName/
│   │   │   ├── AppDelegate.swift                   # iOS app delegate
│   │   │   ├── Info.plist                          # iOS app configuration
│   │   │   ├── LaunchScreen.storyboard             # Launch screen
│   │   │   ├── PrivacyInfo.xcprivacy               # Privacy manifest
│   │   │   └── Images.xcassets/                    # iOS app icons and images
│   │   │       └── AppIcon.appiconset/             # App icon set
│   │   ├── YourProjectName.xcodeproj/              # Xcode project file
│   │   ├── YourProjectName.xcworkspace/            # CocoaPods workspace
│   │   ├── Podfile                                 # iOS dependencies
│   │   ├── Podfile.lock                            # Locked dependency versions
│   │   └── .xcode.env                              # Xcode environment variables
│   │
│   └── macos/                       # macOS-specific code and configuration
│       ├── YourProjectName-macOS/
│       │   ├── AppDelegate.h                       # macOS app delegate header
│       │   ├── AppDelegate.mm                      # macOS app delegate implementation
│       │   ├── Info.plist                          # macOS app configuration
│       │   ├── main.m                              # macOS main entry point
│       │   ├── YourProjectName.entitlements        # macOS app entitlements
│       │   ├── Assets.xcassets/                    # macOS app icons and images
│       │   └── Base.lproj/Main.storyboard          # macOS storyboard
│       ├── YourProjectName.xcodeproj/              # Xcode project file
│       ├── YourProjectName.xcworkspace/            # CocoaPods workspace
│       ├── Podfile                                 # macOS dependencies
│       ├── Podfile.lock                            # Locked dependency versions
│       ├── PrivacyInfo.xcprivacy                   # Privacy manifest
│       └── .xcode.env                              # Xcode environment variables
│
├── 🧪 TESTING
│   └── __tests__/                   # Jest test files
│       └── App.test.tsx            # Main app component test example
│
├── 💻 SOURCE CODE
│   ├── src/                        # Your application source code (created by hooks)
│   │   ├── components/             # Reusable UI components
│   │   │   └── index.ts           # Component exports
│   │   ├── screens/                # Screen/page components
│   │   │   └── index.ts           # Screen exports
│   │   ├── utils/                  # Utility functions and helpers
│   │   │   └── index.ts           # Utility exports
│   │   └── types/                  # TypeScript type definitions
│   │       └── index.ts           # Type exports
│   ├── App.tsx                     # Main React Native app component
│   └── index.js                    # App entry point and registration
│
├── ⚙️ CONFIGURATION
│   ├── package.json                # Node.js dependencies, scripts, and metadata
│   ├── tsconfig.json               # TypeScript configuration
│   ├── jest.config.js              # Jest testing framework configuration
│   ├── metro.config.js             # Metro bundler + NativeWind configuration
│   ├── babel.config.js             # Babel transpiler + NativeWind preset
│   ├── app.json                    # React Native app configuration
│   ├── .eslintrc.js                # ESLint linting rules and configuration
│   ├── .eslintignore               # Files to ignore during linting
│   ├── .prettierrc.js              # Prettier code formatting rules
│   ├── .watchmanconfig             # Watchman file watching configuration
│   └── .gitignore                  # Git version control ignore patterns
│
├── 🎨 STYLING
│   ├── tailwind.config.js          # Tailwind CSS configuration
│   ├── global.css                  # Tailwind CSS directives and global styles
│   └── nativewind-env.d.ts         # NativeWind TypeScript definitions
│
├── 🔧 DEVELOPMENT TOOLS
│   ├── Gemfile                     # Ruby gems for iOS development tools
│   ├── Gemfile.lock                # Locked Ruby gem versions
│   └── README.md                   # Project documentation and setup guide
│
└── 📄 PROJECT INFO
    └── LICENSE                     # Project license file (if selected)
```

### Key Files and Their Purposes

#### Core Application Files
- **[`App.tsx`](App.tsx)**: Main React Native component, app entry point
- **[`index.js`](index.js)**: App registration with React Native
- **[`src/`](src/)**: Organized source code directory structure

#### Configuration Files
- **[`package.json`](package.json)**: Dependencies, scripts, project metadata
- **[`tsconfig.json`](tsconfig.json)**: TypeScript compiler configuration
- **[`metro.config.js`](metro.config.js)**: Metro bundler with NativeWind integration
- **[`babel.config.js`](babel.config.js)**: Babel transpiler with React Native + NativeWind presets

#### Styling System
- **[`tailwind.config.js`](tailwind.config.js)**: Tailwind CSS configuration with NativeWind preset
- **[`global.css`](global.css)**: Tailwind CSS base directives
- **[`nativewind-env.d.ts`](nativewind-env.d.ts)**: TypeScript definitions for className props

#### Development Tools
- **[`.eslintrc.js`](.eslintrc.js)**: ESLint configuration with React Native rules
- **[`.prettierrc.js`](.prettierrc.js)**: Prettier formatting configuration
- **[`jest.config.js`](jest.config.js)**: Jest testing framework setup

#### Platform Directories
- **[`ios/`](ios/)**: Complete iOS app configuration and native code
- **[`android/`](android/)**: Complete Android app configuration and native code  
- **[`macos/`](macos/)**: Complete macOS app configuration and native code

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Template Generation Issues

**Problem**: `cookiecutter: command not found`
```bash
# Solution: Install cookiecutter
pip install cookiecutter

# Or using pipx for isolated installation
pipx install cookiecutter
```

**Problem**: Python version compatibility
```bash
# Check Python version
python --version

# Install Python 3.7+ if needed
# macOS: brew install python
# Ubuntu: sudo apt update && sudo apt install python3 python3-pip
# Windows: Download from python.org
```

**Problem**: Git authentication issues
```bash
# Use HTTPS instead of SSH
cookiecutter https://github.com/jordyvandomselaar/react-native-macos-blank-template

# Or use GitHub shorthand format
cookiecutter gh:jordyvandomselaar/react-native-macos-blank-template

# Or authenticate with GitHub CLI
gh auth login
```

#### Post-Generation Setup Issues

**Problem**: Node.js version mismatch
```bash
# Check current Node.js version
node --version

# Install Node.js 18+ using nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

**Problem**: npm install fails
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

**Problem**: CocoaPods installation fails (macOS)
```bash
# Install CocoaPods using gem
sudo gem install cocoapods

# If gem install fails, try using Homebrew
brew install cocoapods

# Update CocoaPods repo
pod repo update
```

#### Platform-Specific Issues

**iOS Build Problems:**
```bash
# Clean iOS build
cd ios && xcodebuild clean && cd ..

# Reinstall pods
cd ios && pod deintegrate && pod install && cd ..

# Reset iOS Simulator
xcrun simctl erase all

# Update Xcode Command Line Tools
xcode-select --install
```

**Android Build Problems:**
```bash
# Clean Android build
cd android && ./gradlew clean && cd ..

# Reset Metro cache
npx react-native start --reset-cache

# Check Android SDK installation
npx react-native doctor

# Ensure ANDROID_HOME is set
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

**macOS Build Problems:**
```bash
# Clean macOS build
cd macos && xcodebuild clean && cd ..

# Reinstall macOS pods
cd macos && pod deintegrate && pod install && cd ..

# Check macOS-specific dependencies
npx react-native run-macos --verbose
```

#### Metro Bundler Issues

**Problem**: Metro cache corruption
```bash
# Reset Metro cache
npx react-native start --reset-cache

# Clear all caches
rm -rf node_modules
rm -rf $TMPDIR/react-*
rm -rf $TMPDIR/metro-*
npm install
```

**Problem**: Port already in use
```bash
# Kill process on port 8081
npx react-native start --port 8082

# Or kill existing Metro process
lsof -ti:8081 | xargs kill
```

#### NativeWind Styling Issues

**Problem**: Tailwind classes not working
```bash
# Verify global.css is imported in App.tsx
# Should contain: import './global.css';

# Check tailwind.config.js content paths
# Should include your source files

# Reset Metro cache
npx react-native start --reset-cache
```

**Problem**: TypeScript errors with className
```bash
# Ensure nativewind-env.d.ts is present and contains:
# /// <reference types="nativewind/types" />

# Check tsconfig.json includes nativewind-env.d.ts
```

### Environment Verification Commands

```bash
# Check React Native environment
npx react-native doctor

# Verify versions
node --version          # Should be 18+
npm --version           # Latest
python --version        # 3.7+
cookiecutter --version  # Latest

# macOS only
xcode-select --version  # Latest
pod --version           # 1.10.0+

# Android only
java --version          # 11+
adb --version           # Latest
```

### Getting Help

If you encounter issues not covered here:

1. **Check the generated project's README.md** for project-specific instructions
2. **Run `npx react-native doctor`** to identify environment issues
3. **Check React Native documentation** at https://reactnative.dev/docs/troubleshooting
4. **Review NativeWind documentation** at https://nativewind.dev/getting-started/troubleshooting
5. **Check platform-specific guides**:
   - iOS: https://reactnative.dev/docs/running-on-device-ios
   - Android: https://reactnative.dev/docs/running-on-device-android
   - macOS: https://microsoft.github.io/react-native-windows/docs/rnm-getting-started

## ✨ Features

### Development Experience

- **🚀 Fast Refresh**: Instant updates during development without losing state
- **🔥 Hot Reloading**: Automatic app reload when files change
- **🧪 Testing Ready**: Jest configuration with React Native testing utilities
- **🔍 Code Quality**: ESLint and Prettier configured with React Native best practices
- **📱 Multi-Platform**: Single codebase for iOS, Android, and macOS
- **⚡ Performance**: Optimized Metro bundler configuration

### Modern Tooling

- **TypeScript**: Full type safety with strict configuration
- **NativeWind**: Tailwind CSS utility classes for React Native
- **Metro**: Fast JavaScript bundler optimized for React Native
- **Babel**: Modern JavaScript transpilation with React Native preset
- **Watchman**: Efficient file watching for development
- **CocoaPods**: iOS and macOS dependency management

### Build System

- **Gradle**: Android build system with optimization
- **Xcode**: iOS and macOS build integration
- **Metro**: Bundling with tree shaking and optimization
- **Code Splitting**: Automatic bundle optimization
- **Source Maps**: Debug support with source mapping

### Styling System

- **NativeWind Integration**: Tailwind CSS classes via className prop
- **Dark Mode Support**: Built-in dark mode with `dark:` prefix classes
- **Responsive Design**: Platform-specific styling capabilities
- **TypeScript Support**: Full IntelliSense for Tailwind classes
- **Custom Themes**: Extensible Tailwind configuration

### Project Organization

- **Structured Layout**: Organized src/ directory with logical separation
- **Platform Extensions**: Support for .ios.tsx, .android.tsx, .macos.tsx files
- **Index Exports**: Clean import/export patterns
- **Type Definitions**: Centralized TypeScript type management

## 📚 Examples

### Complete Workflow Example

Here's a complete example of using the template from start to finish:

#### 1. Generate Project
```bash
# Install cookiecutter if not already installed
pip install cookiecutter

# Generate project from template
cookiecutter gh:jordyvandomselaar/react-native-macos-blank-template

# Interactive prompts:
project_name [MyReactNativeApp]: WeatherApp
display_name [My React Native App]: Weather Pro
package_id [com.company.myreactnativeapp]: com.weatherpro.app
version [1.0.0]: 1.0.0
author_name [Your Name]: Alex Developer
author_email [your.email@example.com]: alex@weatherpro.com
description [A new React Native multi-platform application]: Professional weather app with forecasts
react_native_version [0.78.2]: 0.78.2
node_version [>=18.0.0]: >=18.0.0
Select license:
1 - MIT
Choose from 1, 2, 3, 4, 5 [1]: 1
```

#### 2. Post-Generation Setup
```bash
# Navigate to project (created automatically)
cd WeatherApp

# Dependencies installed automatically by hooks
# ✅ npm install completed
# ✅ iOS pod install completed  
# ✅ macOS pod install completed
# ✅ Project structure created
```

#### 3. Development Workflow
```bash
# Start Metro bundler
npm start

# In new terminal - Run on iOS
npm run ios
# App opens in iOS Simulator

# In new terminal - Run on Android  
npm run android
# App opens in Android Emulator

# In new terminal - Run on macOS
npm run macos
# App opens as macOS application
```

#### 4. Code Development Example
```tsx
// src/components/WeatherCard.tsx
import React from 'react';
import { View, Text } from 'react-native';

interface WeatherCardProps {
  temperature: number;
  condition: string;
  location: string;
}

export function WeatherCard({ temperature, condition, location }: WeatherCardProps) {
  return (
    <View className="bg-white dark:bg-gray-800 rounded-xl p-6 m-4 shadow-lg">
      <Text className="text-2xl font-bold text-gray-800 dark:text-white">
        {temperature}°
      </Text>
      <Text className="text-lg text-gray-600 dark:text-gray-300 mt-2">
        {condition}
      </Text>
      <Text className="text-sm text-gray-500 dark:text-gray-400 mt-1">
        {location}
      </Text>
    </View>
  );
}
```

```tsx
// App.tsx - Using the component
import React from 'react';
import { SafeAreaView, ScrollView } from 'react-native';
import { WeatherCard } from './src/components/WeatherCard';
import './global.css';

function App() {
  return (
    <SafeAreaView className="flex-1 bg-blue-50 dark:bg-gray-900">
      <ScrollView className="flex-1">
        <WeatherCard 
          temperature={72}
          condition="Sunny"
          location="San Francisco, CA"
        />
        <WeatherCard 
          temperature={68}
          condition="Partly Cloudy"
          location="New York, NY"
        />
      </ScrollView>
    </SafeAreaView>
  );
}

export default App;
```

#### 5. Testing Example
```tsx
// __tests__/WeatherCard.test.tsx
import React from 'react';
import { render, screen } from '@testing-library/react-native';
import { WeatherCard } from '../src/components/WeatherCard';

describe('WeatherCard', () => {
  it('displays weather information correctly', () => {
    render(
      <WeatherCard 
        temperature={75}
        condition="Sunny"
        location="Los Angeles, CA"
      />
    );

    expect(screen.getByText('75°')).toBeTruthy();
    expect(screen.getByText('Sunny')).toBeTruthy();
    expect(screen.getByText('Los Angeles, CA')).toBeTruthy();
  });
});
```

```bash
# Run tests
npm test

# Run with coverage
npm run test -- --coverage
```

#### 6. Quality Assurance
```bash
# Run linting
npm run lint

# Fix auto-fixable issues
npm run lint -- --fix

# Check TypeScript types
npx tsc --noEmit

# Run all quality checks
npm run lint && npm test && npx tsc --noEmit
```

### Example Variable Inputs and Outputs

#### Input Variables
```json
{
  "project_name": "FitnessTracker",
  "display_name": "Fitness Tracker Pro",
  "package_id": "com.fitness.tracker",
  "version": "2.1.0",
  "author_name": "Sarah Johnson",
  "author_email": "sarah@fitnesstracker.com",
  "description": "Advanced fitness tracking app with workout analytics",
  "react_native_version": "0.78.2",
  "node_version": ">=18.0.0",
  "license": "MIT"
}
```

#### Generated Output Structure
```
FitnessTracker/
├── package.json                    # Contains "name": "FitnessTracker"
├── App.tsx                         # Imports './global.css'
├── ios/FitnessTracker/Info.plist   # Contains "Fitness Tracker Pro"
├── android/app/src/main/res/values/strings.xml  # App name
├── android/app/src/main/java/com/fitness/tracker/  # Package structure
└── README.md                       # Customized project documentation
```

#### Generated package.json Example
```json
{
  "name": "FitnessTracker",
  "version": "2.1.0",
  "description": "Advanced fitness tracking app with workout analytics",
  "author": {
    "name": "Sarah Johnson",
    "email": "sarah@fitnesstracker.com"
  },
  "scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios",
    "macos": "react-native run-macos",
    "start": "react-native start",
    "test": "jest",
    "lint": "eslint ."
  },
  "dependencies": {
    "react": "19.0.0",
    "react-native": "0.78.2",
    "react-native-macos": "^0.78.3",
    "nativewind": "^4.1.23",
    "tailwindcss": "^3.4.17"
  }
}
```

This comprehensive README provides everything developers need to successfully use your React Native cookiecutter template, from initial setup through advanced development workflows.
