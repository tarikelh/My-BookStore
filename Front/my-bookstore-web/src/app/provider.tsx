'use client';

import { Provider } from 'react-redux';
import store from '@/store';
import BaseTemplate from '@/components/templates/BaseTemplate/BaseTemplate';

export function Providers({children}) {
    return (
        <Provider store={store}>
            <BaseTemplate>
                {children}
            </BaseTemplate>
        </Provider>
    )
}