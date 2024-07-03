import BaseService from './common/CrudService';
import { Product } from '../types/Product';

class ProductService extends BaseService<Product> {
  get endpoint(): string {
    return '/products';
  }
}

export default new ProductService();