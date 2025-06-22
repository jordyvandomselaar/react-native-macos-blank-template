# React Native Multi-Platform Cookiecutter Template

A comprehensive cookiecutter template for creating React Native applications that support **iOS**, **Android**, and **macOS** platforms with modern tooling and best practices built-in.

## 🚀 Features

- **Multi-Platform Support**: iOS, Android, and macOS out of the box
- **TypeScript**: Full TypeScript support with strict configuration
- **NativeWind**: Tailwind CSS styling for React Native components
- **Modern Tooling**: ESLint, Prettier, Jest pre-configured
- **Metro Configuration**: Optimized bundler setup
- **CocoaPods Integration**: iOS and macOS dependency management
- **Gradle Setup**: Android build system configuration
- **Testing Framework**: Jest with React Native testing utilities

## 📋 Prerequisites

Before using this template, ensure you have the following installed:

### Required Tools
- **Python 3.7+** (for cookiecutter)
- **cookiecutter** (`pip install cookiecutter`)
- **Node.js 18+** (for React Native development)
- **Git** (for version control)

### For iOS/macOS Development
- **macOS** (required for iOS/macOS development)
- **Xcode** (latest version from Mac App Store)
- **Xcode Command Line Tools**: `xcode-select --install`
- **CocoaPods**: `sudo gem install cocoapods`

### For Android Development
- **Android Studio** (latest version)
- **Android SDK** (API level 31 or higher)
- **Java Development Kit (JDK)** 11 or higher

### Development Tools
- **Watchman**: `brew install watchman` (macOS) or follow [installation guide](https://facebook.github.io/watchman/docs/install/)

## 🛠 Usage

### 1. Generate Project from Template

```bash
# Using GitHub URL (replace with your actual repository URL)
cookiecutter https://github.com/username/react-native-cookiecutter-template

# Or using local template directory
cookiecutter /path/to/react-native-cookiecutter-template
```

### 2. Template Variables

When you run cookiecutter, you'll be prompted to provide values for these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `project_name` | Project directory name (no spaces, lowercase recommended) | `MyReactNativeApp` |
| `display_name` | Human-readable app display name | `My React Native App` |
| `package_id` | Bundle/package identifier (reverse domain notation) | `com.company.myreactnativeapp` |
| `version` | Initial version number | `1.0.0` |
| `author_name` | Your full name | `John Doe` |
| `author_email` | Your email address | `john.doe@example.com` |
| `description` | Brief project description | `A new React Native multi-platform application` |
| `react_native_version` | React Native version to use | `0.78.2` |
| `node_version` | Minimum Node.js version | `>=18.0.0` |
| `license` | Project license | `MIT`, `Apache-2.0`, `BSD-3-Clause`, `GPL-3.0`, or `None` |

### 3. Example Usage Session

```bash
$ cookiecutter https://github.com/username/react-native-cookiecutter-template

project_name [MyReactNativeApp]: AwesomeApp
display_name [My React Native App]: Awesome Mobile App
package_id [com.company.myreactnativeapp]: com.awesome.mobileapp
version [1.0.0]: 1.0.0
author_name [Your Name]: Jane Smith
author_email [your.email@example.com]: jane.smith@awesome.com
description [A new React Native multi-platform application]: An awesome cross-platform mobile application
react_native_version [0.78.2]: 0.78.2
node_version [>=18.0.0]: >=18.0.0
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
5 - None
Choose from 1, 2, 3, 4, 5 [1]: 1
```

## 📁 Generated Project Structure

After template generation, your project will have this structure:

```
YourProject/
├── android/                     # Android-specific code and configuration
│   ├── app/
│   │   ├── build.gradle         # Android build configuration
│   │   └── src/main/
│   │       ├── AndroidManifest.xml
│   │       ├── java/com/yourpackage/
│   │       │   ├── MainActivity.kt
│   │       │   └── MainApplication.kt
│   │       └── res/
│   ├── build.gradle             # Project-level build configuration
│   ├── settings.gradle          # Project settings
│   └── gradle.properties        # Gradle properties
├── ios/                         # iOS-specific code and configuration
│   ├── YourProject/
│   │   ├── AppDelegate.swift    # iOS app delegate
│   │   ├── Info.plist          # iOS app configuration
│   │   └── Images.xcassets/     # iOS app icons and images
│   ├── YourProject.xcodeproj/   # Xcode project file
│   ├── YourProject.xcworkspace/ # CocoaPods workspace
│   └── Podfile                  # iOS dependencies
├── macos/                       # macOS-specific code and configuration
│   ├── YourProject-macOS/
│   │   ├── AppDelegate.h
│   │   ├── AppDelegate.mm       # macOS app delegate
│   │   ├── Info.plist          # macOS app configuration
│   │   └── Assets.xcassets/     # macOS app icons and images
│   ├── YourProject.xcodeproj/   # Xcode project file
│   ├── YourProject.xcworkspace/ # CocoaPods workspace
│   └── Podfile                  # macOS dependencies
├── __tests__/                   # Jest test files
│   └── App.test.tsx            # Main app component test
├── App.tsx                      # Main React Native app component
├── index.js                     # App entry point
├── package.json                 # Node.js dependencies and scripts
├── metro.config.js              # Metro bundler + NativeWind configuration
├── babel.config.js              # Babel + NativeWind preset configuration
├── tailwind.config.js           # Tailwind CSS configuration
├── global.css                   # Tailwind CSS directives
├── nativewind-env.d.ts          # NativeWind TypeScript definitions
├── tsconfig.json                # TypeScript configuration
├── jest.config.js               # Jest testing configuration
├── .eslintrc.js                 # ESLint linting rules
├── .prettierrc.js               # Prettier formatting rules
├── .gitignore                   # Git ignore patterns
├── .watchmanconfig              # Watchman configuration
├── app.json                     # React Native app configuration
├── Gemfile                      # Ruby gems for iOS tools
└── README.md                    # Project documentation
```

## 🔧 Post-Generation Setup

After generating your project with cookiecutter, follow these steps:

### 1. Navigate to Project Directory

```bash
cd YourProjectName
```

### 2. Install Dependencies

```bash
# Install Node.js dependencies
npm install

# Install iOS dependencies (macOS only)
cd ios && pod install && cd ..

# Install macOS dependencies (macOS only, if targeting macOS)
cd macos && pod install && cd ..
```

### 3. Platform-Specific Setup

#### iOS Setup
```bash
# Open iOS project in Xcode (optional)
open ios/YourProject.xcworkspace

# Verify iOS simulator is available
xcrun simctl list devices
```

#### Android Setup
```bash
# Open Android project in Android Studio (optional)
# File > Open > YourProject/android

# Verify Android SDK and emulator setup
npx react-native doctor
```

#### macOS Setup
```bash
# Open macOS project in Xcode (optional)
open macos/YourProject.xcworkspace
```

## 🚀 Running Your Application

### Start Metro Bundler (Required)
```bash
# Start the development server
npm start
```

### Run on Different Platforms

#### iOS
```bash
# Run on iOS Simulator
npm run ios

# Run on specific iOS device/simulator
npx react-native run-ios --simulator="iPhone 15 Pro"
npx react-native run-ios --device "Your Device Name"
```

#### Android
```bash
# Run on Android emulator/device
npm run android

# Run on specific Android device
adb devices  # List connected devices
npx react-native run-android --device-id=<device-id>
```

#### macOS
```bash
# Run on macOS
npm run macos
```

## 🧪 Testing Your Application

### Run Tests
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test -- --watch

# Run tests with coverage
npm run test -- --coverage
```

### Linting and Code Quality
```bash
# Run ESLint
npm run lint

# Fix ESLint issues automatically  
npm run lint -- --fix

# Check TypeScript types
npx tsc --noEmit
```

## 🎨 Using NativeWind (Tailwind CSS)

The template includes NativeWind for styling. Here are some examples:

### Basic Usage
```tsx
import React from 'react';
import { View, Text } from 'react-native';
import './global.css';

function MyComponent() {
  return (
    <View className="flex-1 bg-white p-4">
      <Text className="text-lg font-bold text-blue-600">
        Hello NativeWind!
      </Text>
    </View>
  );
}
```

### Dark Mode Support
```tsx
<View className="bg-white dark:bg-gray-900 p-4">
  <Text className="text-gray-800 dark:text-gray-100">
    Auto dark mode text
  </Text>
</View>
```

## 🔍 Troubleshooting

### Common Issues

#### Metro Cache Issues
```bash
# Clear Metro cache
npx react-native start --reset-cache
```

#### iOS Build Issues
```bash
# Clean iOS build
cd ios && xcodebuild clean && cd ..

# Reinstall pods
cd ios && pod deintegrate && pod install && cd ..
```

#### Android Build Issues
```bash
# Clean Android build
cd android && ./gradlew clean && cd ..
```

#### Node Modules Issues
```bash
# Clean install
rm -rf node_modules package-lock.json
npm install
```

### Environment Verification
```bash
# Check React Native environment
npx react-native doctor

# Check versions
node --version
npm --version
npx react-native --version
```

## 📚 Available Scripts

| Script | Command | Description |
|--------|---------|-------------|
| Start | `npm start` | Start Metro bundler |
| iOS | `npm run ios` | Run on iOS simulator |
| Android | `npm run android` | Run on Android emulator/device |
| macOS | `npm run macos` | Run on macOS |
| Test | `npm test` | Run Jest tests |
| Lint | `npm run lint` | Run ESLint |

## 🛠 Customization

### Adding Dependencies
```bash
# Add a new package
npm install <package-name>

# For packages with native code
npm install <package-name>
cd ios && pod install && cd ..  # iOS
cd macos && pod install && cd .. # macOS (if applicable)
```

### Platform-Specific Code
```tsx
// Use platform extensions
Component.ios.tsx      // iOS-specific
Component.android.tsx  // Android-specific  
Component.macos.tsx    // macOS-specific
Component.tsx          // Default/shared

// Or use Platform API
import { Platform } from 'react-native';

const styles = StyleSheet.create({
  container: {
    marginTop: Platform.OS === 'ios' ? 20 : 0,
  },
});
```

## 📄 License Template

Based on your license selection during template generation:

- **MIT**: Permissive license allowing commercial use
- **Apache-2.0**: Patent protection and contributor licensing
- **BSD-3-Clause**: Simple permissive license with attribution
- **GPL-3.0**: Copyleft license requiring source disclosure
- **None**: No license specified

## 🤝 Contributing to the Template

To contribute to this cookiecutter template:

1. Fork the template repository
2. Create a feature branch
3. Make your changes
4. Test with `cookiecutter /path/to/your/template`
5. Submit a pull request

## 📞 Support

- **React Native Documentation**: https://reactnative.dev/docs/getting-started
- **NativeWind Documentation**: https://nativewind.dev
- **Cookiecutter Documentation**: https://cookiecutter.readthedocs.io/

---

**Happy coding! 🎉**