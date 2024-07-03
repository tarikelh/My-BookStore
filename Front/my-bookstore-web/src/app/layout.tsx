'use client';
import "./globals.css";
import BaseTemplate from '../components/templates/BaseTemplate/BaseTemplate';
import { Providers } from "./provider";
import store from '@/store';

const RootLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <html lang="en">
      <head />
      <body>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
};

export default RootLayout;